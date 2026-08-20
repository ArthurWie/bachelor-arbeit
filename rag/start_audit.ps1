# Zellen-Audit starten: API + Frontend + Browser auf der Audit-Ansicht.
# Beenden: dieses Fenster schließen (stoppt beide Kindprozesse).
$rag = $PSScriptRoot
$api = Start-Process -FilePath "$rag\.venv\Scripts\python.exe" `
    -ArgumentList "-m", "uvicorn", "api.main:app", "--port", "8000" `
    -WorkingDirectory $rag -PassThru -WindowStyle Hidden
$vite = Start-Process -FilePath "cmd.exe" `
    -ArgumentList "/c", "npx vite --port 5173 --strictPort" `
    -WorkingDirectory "$rag\frontend" -PassThru -WindowStyle Hidden
Start-Sleep -Seconds 4
Start-Process "http://localhost:5173/?view=audit"
Write-Host "Zellen-Audit läuft: http://localhost:5173/?view=audit"
Write-Host "Urteile landen in corpus\author_audit.csv. Enter beendet beide Server."
Read-Host | Out-Null
Stop-Process -Id $api.Id -Force -ErrorAction SilentlyContinue
Stop-Process -Id $vite.Id -Force -ErrorAction SilentlyContinue
