# Einmaliges Setup auf dem Windows-Rechner (RTX 4060).
# Ausführen im Projektordner:  powershell -ExecutionPolicy Bypass -File scripts\setup_windows.ps1
$ErrorActionPreference = "Stop"

Write-Host "== library-rag Setup ==" -ForegroundColor Green

# 1. uv (Python-Paketmanager) installieren, falls nicht vorhanden
if (-not (Get-Command uv -ErrorAction SilentlyContinue)) {
    Write-Host "Installiere uv ..."
    irm https://astral.sh/uv/install.ps1 | iex
    $env:Path = "$env:USERPROFILE\.local\bin;$env:Path"
}

# 2. Virtuelle Umgebung mit Python 3.12
uv venv --python 3.12 .venv
$py = ".venv\Scripts\python.exe"

# 3. WICHTIG: CUDA-Build von PyTorch ZUERST installieren.
#    Das normale PyPI-Wheel ist auf Windows CPU-only -> das System würde
#    absichtlich anhalten ("CUDA nicht verfügbar").
uv pip install --python $py torch --index-url https://download.pytorch.org/whl/cu128

# 4. Restliche Abhängigkeiten (torch ist schon erfüllt und bleibt unberührt)
uv pip install --python $py -e . --group dev

# 5. Frontend: bewusst nicht installiert. Der Reader ist nicht Teil des
#    Umfangs (siehe RAG_INTEGRATION_PLAN.md); bbox/coord_origin landen aber
#    weiter in der DB. Nachrüsten: cd frontend; npm install; npm run dev
Write-Host "Frontend uebersprungen (nicht im Umfang)." -ForegroundColor DarkGray

# 6. Selbsttest (braucht weder GPU noch Zotero)
& $py -m pytest tests -q

# 7. CUDA-Check
& $py -c "import torch; ok = torch.cuda.is_available(); print('CUDA verfuegbar:', ok, '| GPU:', torch.cuda.get_device_name(0) if ok else '-'); exit(0 if ok else 1)"

Write-Host ""
Write-Host "Setup fertig. Naechste Schritte: siehe README.md Abschnitt 'Ablauf'." -ForegroundColor Green
