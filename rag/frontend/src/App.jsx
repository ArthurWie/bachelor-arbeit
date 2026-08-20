import { BookOpenText, ListChecks, MagnifyingGlass } from '@phosphor-icons/react'
import { useEffect, useState } from 'react'
import { api } from './api.js'
import AuditView from './AuditView.jsx'
import PdfReader from './PdfReader.jsx'

function authorsShort(authors) {
  if (!authors?.length) return 'o. A.'
  const last = authors[0].split(' ').at(-1)
  return authors.length === 1 ? last : `${last} et al.`
}

function pages(a, b) {
  return a === b ? `S. ${a}` : `S. ${a}-${b}`
}

export default function App() {
  const [mode, setMode] = useState(
    new URLSearchParams(window.location.search).get('view') === 'audit'
      ? 'audit' : 'library',
  )
  const [docs, setDocs] = useState([])
  const [docsError, setDocsError] = useState(null)
  const [query, setQuery] = useState('')
  const [yearMin, setYearMin] = useState('')
  const [results, setResults] = useState(null)
  const [busy, setBusy] = useState(false)
  const [searchError, setSearchError] = useState(null)
  const [reader, setReader] = useState(null) // {documentId, title, page, highlights}

  useEffect(() => {
    api.documents().then(setDocs).catch((e) => setDocsError(String(e.message || e)))
    const chunkId = new URLSearchParams(window.location.search).get('chunk')
    if (chunkId) openChunk(Number(chunkId))
  }, [])

  async function openChunk(chunkId) {
    try {
      const c = await api.chunk(chunkId)
      setReader({
        documentId: c.document_id,
        title: `${authorsShort(c.authors)} (${c.year ?? 'o. J.'}): ${c.title}`,
        page: c.bbox?.[0]?.page ?? c.page_start,
        highlights: c.bbox ?? [],
      })
    } catch (e) {
      setSearchError(String(e.message || e))
    }
  }

  async function runSearch(e) {
    e?.preventDefault()
    if (!query.trim()) return
    setBusy(true)
    setSearchError(null)
    try {
      setResults(await api.search(query, yearMin))
    } catch (e) {
      setResults(null)
      setSearchError(String(e.message || e))
    } finally {
      setBusy(false)
    }
  }

  if (mode === 'audit') return <AuditView onExit={() => setMode('library')} />

  return (
    <div className="app">
      <aside className="sidebar">
        <div className="brand">
          <h1>Bibliothek</h1>
          <span className="brand-count">{docs.length} Papers</span>
          <button
            className="ctl audit-enter"
            title="Zellen-Audit der Kodiertabelle"
            onClick={() => setMode('audit')}
          >
            <ListChecks size={15} /> Audit
          </button>
        </div>

        <form className="search" onSubmit={runSearch}>
          <input
            value={query}
            onChange={(e) => setQuery(e.target.value)}
            placeholder="Frage an die Bibliothek …"
          />
          <div className="search-row">
            <input
              className="year"
              value={yearMin}
              onChange={(e) => setYearMin(e.target.value.replace(/\D/g, ''))}
              placeholder="ab Jahr"
              inputMode="numeric"
            />
            <button type="submit" disabled={busy}>
              <MagnifyingGlass size={15} weight="bold" />
              {busy ? 'Sucht …' : 'Suchen'}
            </button>
          </div>
        </form>

        {searchError && <div className="banner error">{searchError}</div>}

        {busy && (
          <>
            <div className="section-head"><span>Treffer</span></div>
            <div className="skeleton" aria-hidden="true">
              {[0, 1, 2].map((i) => (
                <div className="skeleton-row" key={i}><i /><i /><i /></div>
              ))}
            </div>
          </>
        )}

        {!busy && results && (
          <section>
            <div className="section-head">
              <span>Treffer</span>
              <span>{results.length}</span>
            </div>
            <div className="results">
              {results.map((r) => (
                <article
                  key={r.chunk_id}
                  className="result"
                  onClick={() => openChunk(r.chunk_id)}
                >
                  <header>
                    <span>
                      {authorsShort(r.authors)} {r.year ?? 'o. J.'} · {pages(r.page_start, r.page_end)}
                    </span>
                    <span className="score">{r.score.toFixed(2)}</span>
                  </header>
                  <p>{r.text.length > 260 ? r.text.slice(0, 260) + '…' : r.text}</p>
                  <footer>{r.section}</footer>
                </article>
              ))}
            </div>
          </section>
        )}

        <section>
          <div className="section-head">
            <span>Dokumente</span>
          </div>
          {docsError && <div className="banner error">{docsError}</div>}
          <div className="docs">
            {docs.map((d) => (
              <button
                key={d.id}
                className={'doc' + (reader?.documentId === d.id ? ' active' : '')}
                onClick={() =>
                  setReader({
                    documentId: d.id,
                    title: `${authorsShort(d.authors)} (${d.year ?? 'o. J.'}): ${d.title}`,
                    page: 1,
                    highlights: [],
                  })
                }
              >
                <span className="doc-year">{d.year ?? '·'}</span>
                <span className="doc-title">{d.title}</span>
                {!d.n_chunks && <span className="doc-flag">nicht indexiert</span>}
              </button>
            ))}
          </div>
        </section>
      </aside>

      <main className="main">
        {reader ? (
          <PdfReader {...reader} />
        ) : (
          <div className="empty">
            <BookOpenText size={30} weight="thin" />
            <p>Ein Dokument öffnen oder die Bibliothek durchsuchen. Treffer führen direkt zur zitierten Stelle im PDF.</p>
          </div>
        )}
      </main>
    </div>
  )
}
