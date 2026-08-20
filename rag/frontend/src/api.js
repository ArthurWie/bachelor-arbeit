async function json(res) {
  if (!res.ok) {
    const body = await res.text().catch(() => '')
    throw new Error(`${res.status} ${res.statusText}${body ? ` – ${body.slice(0, 200)}` : ''}`)
  }
  return res.json()
}

export const api = {
  documents: () => fetch('/api/documents').then(json),
  search: (query, yearMin) =>
    fetch('/api/search', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({
        query,
        filters: yearMin ? { year_min: Number(yearMin) } : null,
      }),
    }).then(json),
  chunk: (id) => fetch(`/api/chunks/${id}`).then(json),
  fileUrl: (documentId) => `/api/documents/${documentId}/file`,
  auditQueue: () => fetch('/api/audit/queue').then(json),
  auditVerdict: (study_id, column, verdict, note = '') =>
    fetch('/api/audit/verdict', {
      method: 'POST',
      headers: { 'Content-Type': 'application/json' },
      body: JSON.stringify({ study_id, column, verdict, note }),
    }).then(json),
}
