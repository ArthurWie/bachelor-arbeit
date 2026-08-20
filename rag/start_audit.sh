#!/usr/bin/env bash
# Zellen-Audit auf dem Mac starten: API + Frontend + Browser auf der Audit-Ansicht.
# Beenden: Ctrl+C (stoppt beide Kindprozesse).
set -e
rag="$(cd "$(dirname "$0")" && pwd)"

"$rag/.venv/bin/python" -m uvicorn api.main:app --port 8000 --app-dir "$rag" &
api_pid=$!
(cd "$rag/frontend" && npx vite --port 5173 --strictPort) &
vite_pid=$!
trap 'kill $api_pid $vite_pid 2>/dev/null' EXIT

sleep 4
open "http://localhost:5173/?view=audit"
echo "Zellen-Audit läuft: http://localhost:5173/?view=audit"
echo "Urteile landen in corpus/author_audit.csv. Ctrl+C beendet beide Server."
wait
