$ScriptDir = Split-Path -Parent $MyInvocation.MyCommand.Definition
$Frontend = Join-Path $ScriptDir "frontend\index.html"

Start-Process python "$ScriptDir\master-data\app\main.py"
Start-Process python "$ScriptDir\orders\app\main.py"
Start-Process python "$ScriptDir\statistics\app\main.py"

Write-Host ""
Write-Host "Servers started."
Write-Host "Open the frontend:"
Write-Host "file:///$Frontend"
Write-Host ""

Read-Host -Prompt "Press Enter to exit"
