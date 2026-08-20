import { ArrowLeft, CheckCircle, Copy, Flag, Question, WarningCircle } from '@phosphor-icons/react'
import { useEffect, useMemo, useRef, useState } from 'react'
import { api } from './api.js'
import PdfReader from './PdfReader.jsx'

const NO_HIGHLIGHTS = [] // stabile Referenz: neue []-Literale würden den Reader zurücksetzen

const A1 = new Set(['country_region', 'sample', 'method', 'ai_measure'])
const A2 = new Set(['outcome_construct', 'performance_measure', 'ca_measure',
  'effect_direction', 'conditions', 'key_finding'])

function tableOf(col) {
  if (A1.has(col)) return 'A.1'
  if (A2.has(col)) return 'A.2'
  return 'nur kodiert'
}

const LEGEND = [
  ['Tabelle A.1 (Studiencharakteristika)', [
    ['country_region', 'Land/Region der untersuchten Firmen (nicht der Autoren!)'],
    ['sample', 'Stichprobe: n + Einheit, ggf. Zeitraum'],
    ['method', 'Studiendesign, das die AI→Erfolg-Evidenz erzeugt'],
    ['ai_measure', 'wie AI-Investition/-Adoption gemessen wird (Messtyp + Kurzerklärung)'],
  ]],
  ['Tabelle A.2 (Befunde)', [
    ['outcome_construct', 'Perf. = Performance · CA = Competitive Advantage · Both = beides eigenständig gemessen (Betreuer-Feedback: strikt trennen)'],
    ['performance_measure', 'konkretes Performance-Maß (ROA, Tobin’s q, Survey-Skala …)'],
    ['ca_measure', 'eigenes CA-Konstrukt — nur wenn wirklich als eigenes Konstrukt gemessen; meist leer, und diese Leere ist selbst ein Befund'],
    ['effect_direction', 'positive / negative · mixed = je Ergebnisgröße geteilt · conditional = Effekt existiert NUR unter Bedingungen (volle Mediation, Schwelle, Null-Basiseffekt)'],
    ['conditions', 'identifizierte Moderatoren, Mediatoren, Komplemente, Schwellen — die Kernspalte der Arbeit'],
    ['key_finding', 'zentrales Ergebnis der Studie in einem Satz (eigene Worte)'],
  ]],
  ['Nicht gedruckt (nur Kodierdaten)', [
    ['theoretical_lens', 'Theorie(n), die die Studie selbst verwendet'],
    ['industry', 'Branche oder cross-industry'],
    ['quality_notes', 'Evidenzqualität (Selbstauskunft? Panel? kleines n?) — teils Koder-Kommentar ohne Belegstelle'],
  ]],
  ['Symbole', [
    ['✓ / ⚠ / ✗', 'Zitat maschinell auf der PDF-Seite bestätigt / auf der Seite nicht bestätigt (Seite ansehen) / nicht im Text'],
    ['kodiert (Rohwert)', 'grauer Text unter der Zelle = ursprünglicher Kodierwert; oben steht der gedruckte (verdichtete) Wortlaut'],
    ['Dossier-Flag', 'Zelle, die beim Evidenz-Dossier bereits als Spannungsfall auffiel (G springt zum nächsten)'],
    ['2. Pass: geändert', 'Zelle, die bei der Flag-Aufarbeitung (20. Aug) korrigiert oder neu belegt wurde — nur diese nachprüfen, G springt auch hierhin'],
  ]],
]

/**
 * Zellen-Audit: ein Schritt = eine Zelle der Kodiertabelle, PDF springt zur
 * Belegstelle und hebt sie hervor. Leertaste/Enter = Zelle OK + weiter,
 * F = Flag mit Notiz, Pfeile = Navigation, U = Urteil aufheben, G = nächstes
 * vorab geflaggtes. Urteile: append-only nach corpus/author_audit.csv.
 */
export default function AuditView({ onExit }) {
  const [steps, setSteps] = useState(null)
  const [verdicts, setVerdicts] = useState({})
  const [idx, setIdx] = useState(0)
  const [quoteIdx, setQuoteIdx] = useState(0)
  const [noteMode, setNoteMode] = useState(false)
  const [note, setNote] = useState('')
  const [jumpKey, setJumpKey] = useState(0)
  const [showLegend, setShowLegend] = useState(false)
  const [searchHit, setSearchHit] = useState(true)
  const [copied, setCopied] = useState(false)
  const [error, setError] = useState(null)
  const noteRef = useRef(null)

  useEffect(() => {
    api.auditQueue().then((q) => {
      setSteps(q.steps)
      setVerdicts(q.verdicts)
      const first = q.steps.findIndex(
        (s) => !q.verdicts[`${s.study_id}|${s.column}`])
      setIdx(first < 0 ? 0 : first)
    }).catch((e) => setError(String(e.message || e)))
  }, [])

  const step = steps?.[idx]
  const key = step ? `${step.study_id}|${step.column}` : null
  const done = useMemo(
    () => steps ? steps.filter((s) => verdicts[`${s.study_id}|${s.column}`]).length : 0,
    [steps, verdicts])
  const flaggedByMe = useMemo(
    () => Object.values(verdicts).filter((v) => v.verdict === 'flag').length,
    [verdicts])

  function goto(i) {
    if (!steps) return
    setIdx(Math.max(0, Math.min(steps.length - 1, i)))
    setQuoteIdx(0)
    setSearchHit(true)
    setCopied(false)
  }

  // Prüf-Prompt für ein externes LLM: gedruckter Zellwert + alle Belegstellen
  function copyPrompt() {
    const quotes = step.quotes.map((q, i) =>
      `[${i + 1}] (${q.printed_pages ? `p. ${q.printed_pages}` : `PDF p. ${q.pdf_page}`}) "${q.quote}"`,
    ).join('\n')
    const text = `Is the following coded value fully supported by the verbatim quotes below from the article — nothing invented, nothing stretched beyond what the quotes say?

Study: ${step.study_id} · ${step.label}
Column: ${step.column}
Coded value: "${(step.printed ?? step.coded) || ''}"

Quotes from the article:
${quotes}

The full article PDF is attached. If the quotes above do not prove the value, search the article yourself before answering: if you find backing elsewhere, answer SUPPORTED and cite the passage verbatim with its page — but still add a FLAG-NOTE, because the recorded quotes need re-pinning.

Answer: SUPPORTED / PARTLY / NOT SUPPORTED, and say exactly which part of the value lacks backing.

If PARTLY or NOT SUPPORTED, or if you had to find the backing yourself, add one final line in exactly this format:
FLAG-NOTE: <one-line question, referencing quote numbers, that prompts a reviewer to take a closer look — e.g. "Does [2] really back the moderation claim, or only a direct effect?">`
    navigator.clipboard.writeText(text).then(() => {
      setCopied(true)
      setTimeout(() => setCopied(false), 1500)
    }).catch((e) => setError(String(e.message || e)))
  }

  async function submit(verdict, noteText = '') {
    if (!step) return
    try {
      await api.auditVerdict(step.study_id, step.column, verdict, noteText)
      setVerdicts((v) => {
        const next = { ...v }
        if (verdict === 'clear') delete next[key]
        else next[key] = { verdict, note: noteText, date: 'heute' }
        return next
      })
      if (verdict !== 'clear') goto(idx + 1)
    } catch (e) {
      setError(String(e.message || e))
    }
  }

  useEffect(() => {
    function onKey(e) {
      if (noteMode) {
        if (e.key === 'Escape') { setNoteMode(false); setNote('') }
        return
      }
      if (showLegend) {
        if (e.key === 'Escape' || e.key === '?') { e.preventDefault(); setShowLegend(false) }
        return // Legende offen: Urteils-Tasten inaktiv
      }
      if (e.target.tagName === 'INPUT' || e.target.tagName === 'TEXTAREA') return
      if (e.key === '?') { e.preventDefault(); setShowLegend(true); return }
      if (e.key === ' ' || e.key === 'Enter') { e.preventDefault(); submit('ok') }
      else if (e.key === 'f' || e.key === 'F') { e.preventDefault(); setNoteMode(true) }
      else if (e.key === 'ArrowLeft') goto(idx - 1)
      else if (e.key === 'ArrowRight') goto(idx + 1)
      else if (e.key === 'u' || e.key === 'U') submit('clear')
      else if (e.key === 'g' || e.key === 'G') {
        const next = steps.findIndex((s, i) => i > idx && (s.flagged || s.recheck))
        if (next > -1) goto(next)
      } else if (/^[1-9]$/.test(e.key)) {
        const q = Number(e.key) - 1
        if (step && q < step.quotes.length) {
          setQuoteIdx(q)
          setSearchHit(true)
          setJumpKey((k) => k + 1) // auch bei gleicher Belegstelle zurückspringen
        }
      }
    }
    window.addEventListener('keydown', onKey)
    return () => window.removeEventListener('keydown', onKey)
  })

  useEffect(() => { if (noteMode) noteRef.current?.focus() }, [noteMode])

  if (error) return <div className="banner error">{error}</div>
  if (!steps) return <div className="empty"><p>Lade Audit-Queue …</p></div>
  if (!step) return <div className="empty"><p>Queue leer.</p></div>

  const quote = step.quotes[quoteIdx]
  const myVerdict = verdicts[key]

  return (
    <div className="app audit">
      <aside className="sidebar audit-side">
        <div className="brand">
          <button className="ctl" onClick={onExit} aria-label="Zurück zur Bibliothek">
            <ArrowLeft size={15} />
          </button>
          <h1>Zellen-Audit</h1>
          <span className="brand-count">{done} / {steps.length}</span>
          <button
            className="ctl"
            onClick={() => setShowLegend(true)}
            aria-label="Legende (Taste ?)"
            title="Legende (Taste ?)"
          >
            <Question size={15} />
          </button>
        </div>
        <div className="audit-progress">
          <div className="audit-progress-fill" style={{ width: `${(100 * done) / steps.length}%` }} />
        </div>

        <div className="audit-step">
          <div className="audit-study">{step.study_id} · {step.label}</div>
          <div className="audit-col">
            <span className="audit-table-tag">{tableOf(step.column)}</span>
            <strong>{step.column}</strong>
            {step.flagged && <span className="audit-flag-tag"><WarningCircle size={13} /> Dossier-Flag</span>}
            {step.recheck && <span className="audit-flag-tag audit-recheck"><WarningCircle size={13} /> 2. Pass: geändert</span>}
            {step.quotes.length > 0 && (
              <button
                className="audit-copy"
                onClick={copyPrompt}
                title="Prüf-Prompt (Zellwert + Belegstellen) in die Zwischenablage"
              >
                {copied ? <CheckCircle size={13} /> : <Copy size={13} />}
                {copied ? 'kopiert' : 'Prompt'}
              </button>
            )}
          </div>
          <div className="audit-coded">{(step.printed ?? step.coded) || <em>— leer kodiert —</em>}</div>
          {step.printed && step.printed !== step.coded && (
            <div className="audit-raw">kodiert (Rohwert): {step.coded}</div>
          )}
        </div>

        <div className="audit-quotes">
          {step.quotes.length === 0 && (
            <p className="audit-noquote">Keine Belegstelle (Koder-Kommentar) — Zelle inhaltlich prüfen.</p>
          )}
          {step.quotes.map((q, i) => (
            <article
              key={i}
              className={'result audit-quote' + (i === quoteIdx ? ' active' : '')}
              onClick={() => { setQuoteIdx(i); setSearchHit(true); setJumpKey((k) => k + 1) }}
            >
              <header>
                <span>[{i + 1}] {q.printed_pages ? `S. ${q.printed_pages}` : `PDF-S. ${q.pdf_page}`}</span>
                <span>{q.verdict === 'verified' ? '✓' : q.verdict === 'page-unconfirmed' ? '⚠' : '✗'}</span>
              </header>
              <p>{q.quote}</p>
              {q.tension && <footer className="audit-tension">⚠ {q.tension}</footer>}
            </article>
          ))}
          {step.row_note && <p className="audit-rownote">Dossier-Notiz: {step.row_note}</p>}
          {!searchHit && quote && (
            <p className="audit-nohit">Passage im Textlayer nicht gefunden — Seite {quote.pdf_page} ist geöffnet, Zitat links mit dem Auge abgleichen.</p>
          )}
        </div>

        {noteMode ? (
          <form
            className="audit-noteform"
            onSubmit={(e) => {
              e.preventDefault()
              const t = note.trim()
              setNoteMode(false)
              setNote('')
              submit('flag', t)
            }}
          >
            <input
              ref={noteRef}
              value={note}
              onChange={(e) => setNote(e.target.value)}
              placeholder="Was stimmt nicht? (Enter = Flag, Esc = abbrechen)"
            />
          </form>
        ) : (
          <div className="audit-keys">
            {myVerdict && (
              <span className={'audit-verdict ' + myVerdict.verdict}>
                {myVerdict.verdict === 'ok' ? <CheckCircle size={14} /> : <Flag size={14} />}
                {myVerdict.verdict === 'ok' ? 'OK' : `Flag: ${myVerdict.note}`}
              </span>
            )}
            <span><kbd>Leertaste</kbd> OK + weiter</span>
            <span><kbd>F</kbd> Flag + Notiz</span>
            <span><kbd>←</kbd>/<kbd>→</kbd> blättern</span>
            <span><kbd>U</kbd> Urteil aufheben</span>
            <span><kbd>G</kbd> nächstes Dossier-Flag</span>
            <span><kbd>1</kbd>–<kbd>{step.quotes.length || 1}</kbd> Belegstelle</span>
            <span><kbd>?</kbd> Legende</span>
            {flaggedByMe > 0 && <span className="audit-flagcount">{flaggedByMe} geflaggt</span>}
          </div>
        )}
      </aside>

      <main className="main">
        {quote ? (
          <PdfReader
            documentId={step.document_id}
            title={`${step.study_id} · ${step.label}`}
            page={quote.pdf_page}
            highlights={NO_HIGHLIGHTS}
            searchText={quote.ctrl_f || quote.quote}
            onSearchResult={setSearchHit}
            jumpKey={jumpKey}
          />
        ) : (
          <PdfReader
            documentId={step.document_id}
            title={`${step.study_id} · ${step.label}`}
            page={1}
            highlights={NO_HIGHLIGHTS}
          />
        )}
      </main>

      {showLegend && (
        <div className="legend-overlay" onClick={() => setShowLegend(false)}>
          <div className="legend" onClick={(e) => e.stopPropagation()}>
            <h2>Spalten &amp; Symbole</h2>
            {LEGEND.map(([group, items]) => (
              <section key={group}>
                <h3>{group}</h3>
                <dl>
                  {items.map(([term, desc]) => (
                    <div key={term}>
                      <dt>{term}</dt>
                      <dd>{desc}</dd>
                    </div>
                  ))}
                </dl>
              </section>
            ))}
            <p className="legend-close"><kbd>Esc</kbd> oder Klick außerhalb schließt.</p>
          </div>
        </div>
      )}
    </div>
  )
}
