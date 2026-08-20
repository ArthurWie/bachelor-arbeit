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
/**
 * Sucht searchText (whitespace-normalisiert, case-insensitiv) im Textlayer der
 * Seite und liefert Overlay-Rechtecke der beteiligten Text-Items. Leeres
 * Ergebnis = nicht gefunden (Ligatur-/Extraktionsdifferenz) — der Aufrufer
 * zeigt dann nur die Seite.
 */
function findTextRects(textContent, searchText, viewport) {
  const norm = (s) => s.toLowerCase().replace(/\s+/g, ' ').trim()
  const target = norm(searchText || '')
  if (!target) return []
  let concat = ''
  const spans = []
  for (const item of textContent.items) {
    const t = norm(item.str)
    if (!t) continue
    const start = concat ? concat.length + 1 : 0
    concat = concat ? `${concat} ${t}` : t
    spans.push({ start, end: concat.length, item })
  }
  let pos = concat.indexOf(target)
  let len = target.length
  if (pos < 0) {
    // zweiter Versuch ohne jedes Leerzeichen (getrennte Ligaturen, Kerning)
    const tight = (s) => s.replace(/ /g, '')
    const tPos = tight(concat).indexOf(tight(target))
    if (tPos < 0) return []
    // tight-Position zurück auf concat-Position abbilden
    let seen = 0
    for (let i = 0; i < concat.length; i++) {
      if (concat[i] !== ' ') {
        if (seen === tPos) { pos = i; break }
        seen++
      }
    }
    len = tight(target).length
    let count = 0
    let end = pos
    while (end < concat.length && count < len) {
      if (concat[end] !== ' ') count++
      end++
    }
    len = end - pos
  }
  const endPos = pos + len
  return spans
    .filter((s) => s.end > pos && s.start < endPos)
    .map(({ item }) => {
      const x = item.transform[4]
      const y = item.transform[5]
      const [ax, ay] = viewport.convertToViewportPoint(x, y - 2)
      const [bx, by] = viewport.convertToViewportPoint(x + item.width, y + item.height + 2)
      return {
        left: Math.min(ax, bx),
        top: Math.min(ay, by),
        width: Math.abs(bx - ax),
        height: Math.abs(by - ay),
      }
    })
}

export default function PdfReader({ documentId, title, page, highlights, searchText, onSearchResult, jumpKey }) {
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

  // Nur bei echtem Zielwechsel (oder explizitem Sprung via jumpKey) zur
  // Zielseite springen — freies Blättern wird nie zurückgesetzt.
  useEffect(() => {
    setPageNo(page || 1)
  }, [documentId, page, searchText, jumpKey])

  useEffect(() => {
    if (!pdf || !canvasRef.current) return
    let cancelled = false

    pdf.getPage(Math.min(Math.max(1, pageNo), pdf.numPages)).then((pdfPage) => {
      if (cancelled) return
      const viewport = pdfPage.getViewport({ scale, rotation: pdfPage.rotate })
      const canvas = canvasRef.current
      const ctx = canvas.getContext('2d')
      // In physischer Pixeldichte rendern (Windows-Skalierung/HiDPI), sonst
      // wird der Canvas hochgestreckt und die Seite wirkt wie ein unscharfes
      // Bild. Overlays bleiben in CSS-Pixeln — nur der Canvas skaliert.
      const dpr = window.devicePixelRatio || 1
      canvas.width = Math.floor(viewport.width * dpr)
      canvas.height = Math.floor(viewport.height * dpr)
      canvas.style.width = `${Math.floor(viewport.width)}px`
      canvas.style.height = `${Math.floor(viewport.height)}px`

      renderTask.current?.cancel()
      renderTask.current = pdfPage.render({
        canvasContext: ctx,
        viewport,
        transform: dpr !== 1 ? [dpr, 0, 0, dpr, 0, 0] : undefined,
      })
      renderTask.current.promise.catch(() => {}) // cancel ist kein Fehler

      // Gespeicherte bboxes sind relativ zur sichtbaren Seite; PDF-User-Space
      // kann per CropBox verschoben sein -> view-Offset addieren.
      const [ox, oy] = [pdfPage.view[0], pdfPage.view[1]]
      const pageHeight = pdfPage.view[3] - pdfPage.view[1]
      const bboxRects = (highlights || [])
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
        })
      // Suche nur auf der Zitatseite — beim freien Blättern weder fremde
      // Treffer markieren noch das Suchergebnis der Zitatseite überschreiben.
      if (searchText && pageNo === (page || 1)) {
        pdfPage.getTextContent().then((tc) => {
          if (cancelled) return
          const found = findTextRects(tc, searchText, viewport)
          setRects([...bboxRects, ...found])
          onSearchResult?.(found.length > 0)
        }).catch(() => !cancelled && setRects(bboxRects))
      } else {
        setRects(bboxRects)
      }
    }).catch((e) => !cancelled && setError(String(e.message || e)))
    return () => {
      cancelled = true
    }
  }, [pdf, pageNo, scale, highlights, searchText, page])

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
