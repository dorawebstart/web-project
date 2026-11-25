# Автосинхронізація репозиторію навчання.
# Підтягує останні зміни з GitHub. Запускається Планувальником завдань Windows.
$ErrorActionPreference = "SilentlyContinue"

# Корінь репозиторію — на два рівні вище цього скрипта (LEARNING\scripts\)
$repo = Resolve-Path (Join-Path $PSScriptRoot "..\..")
$branch = "claude/learning-plan-courses-yh6kwl"

git -C $repo fetch origin
git -C $repo checkout $branch
git -C $repo pull --rebase --autostash origin $branch
