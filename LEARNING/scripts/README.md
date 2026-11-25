# Автосинхронізація навчання

`sync.ps1` підтягує останні зміни з GitHub на ноутбук автоматично, щоб не
робити `git pull` руками.

## Одноразове налаштування (на ноутбуці)

Відкрий **PowerShell** і встав цю команду один раз (реєструє завдання, що
запускає синхронізацію при вході в систему і далі кожні 15 хвилин):

```powershell
$script = "C:\Users\slayyya\web-project\LEARNING\scripts\sync.ps1"
$action = New-ScheduledTaskAction -Execute "powershell.exe" -Argument "-NoProfile -WindowStyle Hidden -ExecutionPolicy Bypass -File `"$script`""
$atLogon = New-ScheduledTaskTrigger -AtLogOn
$every15 = New-ScheduledTaskTrigger -Once -At (Get-Date) -RepetitionInterval (New-TimeSpan -Minutes 15)
Register-ScheduledTask -TaskName "SyncLearning" -Action $action -Trigger $atLogon,$every15 -Description "Auto git pull learning repo" -Force
```

Після цього нічого робити не треба — зміни приходять самі.

## Перевірити вручну

```powershell
Start-ScheduledTask -TaskName "SyncLearning"
```

## Вимкнути / видалити

```powershell
Unregister-ScheduledTask -TaskName "SyncLearning" -Confirm:$false
```

## Якщо шлях до репозиторію інший

Заміни `C:\Users\slayyya\web-project` у команді вище на свій шлях.
