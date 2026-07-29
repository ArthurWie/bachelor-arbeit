import { CaretLeft, CaretRight, MagnifyingGlassMinus, MagnifyingGlassPlus } from '@phosphor-icons/react'
import * as pdfjsLib from 'pdfjs-dist'
import workerUrl from 'pdfjs-dist/build/pdf.worker.min.mjs?url'
import { useEffect, useRef, useState } from 'react'
import { api } from './api.js'

pdfjsLib.GlobalWorkerOptions.workerSrc = workerUrl

const ZOOMS = [0.75, 1, 1.25, 1.5, 2, 3]

/**
 * PDF-Canvas mit Highlight-Overlays.
 *
 * Koordinaten werden NICHT selbst umgerechnet: convertToViewportPoint()
 * erledigt Y-Spiegelung (PDF-Ursprung unten links vs. Canvas oben links),
 * Zoom und Rotation. Die gespeicherten bboxes sind BOTTOMLEFT (Docling);
 * sollte je ein TOPLEFT-Eintrag auftauchen, wird er vorher in den
 * PDF-User-Space gespiegelt.
 */
export default function PdfReader({ documentId, title, page, highlights }) {
  const [pdf, setPdf] = useState(null)
  const [pageNo, setPageNo] = useState(page || 1)
  const [numPages, setNumPages] = useState(0)
  const [zoomIdx, setZoomIdx] = useState(2)   // Index in ZOOMS, Start 125 %
  const scale = ZOOMS[zoomIdx]
  const [rects, setRects] = useState([])
  const [error, setError] = useState(null)
  const canvasRef = useRef(null)
  const renderTask = useRef(null)

  useEffect(() => {
    let cancelled = false
    setPdf(null)
    setNumPages(0)
    setRects([])
    setError(null)
    const loadingTask = pdfjsLib.getDocument({ url: api.fileUrl(documentId) })
    loadingTask.promise
      .then((doc) => {
        if (cancelled) return
        setPdf(doc)
        setNumPages(doc.numPages)
      })
      .catch((e) => !cancelled && setError(String(e.message || e)))
    return () => {
      cancelled = true
      loadingTask.destroy().catch(() => {}) // beendet Worker + Dokument
    }
  }, [documentId])

  useEffect(() => {
    setPageNo(page || 1)
  }, [documentId, page, highlights])

  useEffect(() => {
    if (!pdf || !canvasRef.current) return
    let cancelled = false

    pdf.getPage(Math.min(Math.max(1, pageNo), pdf.numPages)).then((pdfPage) => {
      if (cancelled) return
      const viewport = pdfPage.getViewport({ scale, rotation: pdfPage.rotate })
      const canvas = canvasRef.current
      const ctx = canvas.getContext('2d')
      canvas.width = Math.floor(viewport.width)
      canvas.height = Math.floor(viewport.height)

      renderTask.current?.cancel()
      renderTask.current = pdfPage.render({ canvasContext: ctx, viewport })
      renderTask.current.promise.catch(() => {}) // cancel ist kein Fehler

      // Gespeicherte bboxes sind relativ zur sichtbaren Seite; PDF-User-Space
      // kann per CropBox verschoben sein -> view-Offset addieren.
      const [ox, oy] = [pdfPage.view[0], pdfPage.view[1]]
      const pageHeight = pdfPage.view[3] - pdfPage.view[1]
      setRects(
        (highlights || [])
          .filter((h) => h.page === pageNo)
          .map((h) => {
            let { x0, y0, x1, y1 } = h
            if ((h.coord_origin || 'BOTTOMLEFT').toUpperCase() !== 'BOTTOMLEFT') {
              const t = y0
              y0 = pageHeight - y1
              y1 = pageHeight - t
            }
            const [ax, ay] = viewport.convertToViewportPoint(x0 + ox, y0 + oy)
            const [bx, by] = viewport.convertToViewportPoint(x1 + ox, y1 + oy)
            return {
              left: Math.min(ax, bx),
              top: Math.min(ay, by),
              width: Math.abs(bx - ax),
              height: Math.abs(by - ay),
            }
          }),
      )
    }).catch((e) => !cancelled && setError(String(e.message || e)))
    return () => {
      cancelled = true
    }
  }, [pdf, pageNo, scale, highlights])

  if (error) return <div className="reader-error">PDF nicht ladbar: {error}</div>

  return (
    <div className="reader">
      <div className="reader-bar">
        <span className="reader-title" title={title}>{title}</span>
      </div>
      <div className="reader-scroll">
        <div className="reader-canvas-wrap">
          <canvas ref={canvasRef} />
          {rects.map((r, i) => (
            <div
              key={i}
              className="highlight"
              style={{ left: r.left, top: r.top, width: r.width, height: r.height }}
            />
          ))}
        </div>
      </div>
      <div className="reader-controls">
        <button
          className="ctl"
          aria-label="Vorige Seite"
          onClick={() => setPageNo((p) => Math.max(1, p - 1))}
          disabled={pageNo <= 1}
        >
          <CaretLeft size={16} />
        </button>
        <span className="reader-page">{pageNo} / {numPages || '…'}</span>
        <button
          className="ctl"
          aria-label="Nächste Seite"
          onClick={() => setPageNo((p) => Math.min(numPages, p + 1))}
          disabled={pageNo >= numPages}
        >
          <CaretRight size={16} />
        </button>
        <span className="gap" />
        <button
          className="ctl"
          aria-label="Verkleinern"
          onClick={() => setZoomIdx((i) => Math.max(0, i - 1))}
          disabled={zoomIdx <= 0}
        >
          <MagnifyingGlassMinus size={16} />
        </button>
        <span className="reader-zoom">{Math.round(scale * 100)} %</span>
        <button
          className="ctl"
          aria-label="Vergrößern"
          onClick={() => setZoomIdx((i) => Math.min(ZOOMS.length - 1, i + 1))}
          disabled={zoomIdx >= ZOOMS.length - 1}
        >
          <MagnifyingGlassPlus size={16} />
        </button>
      </div>
    </div>
  )
}
