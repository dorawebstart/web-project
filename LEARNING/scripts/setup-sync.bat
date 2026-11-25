@echo off
echo Registering auto-sync task "SyncLearning" (every 15 minutes)...
schtasks /create /tn SyncLearning /tr "powershell -NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File \"%~dp0sync.ps1\"" /sc minute /mo 15 /f
echo.
echo Running first sync now...
powershell -NoProfile -ExecutionPolicy Bypass -File "%~dp0sync.ps1"
echo.
schtasks /query /tn SyncLearning
echo.
echo Done. Auto-sync is active. You can close this window.
pause
