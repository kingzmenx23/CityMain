# Apply this City Main frontend update on Windows

**Destination:** `C:\project_city\city-main`

The ZIP is a **drop-in update**, not a replacement for the existing Next.js project. It intentionally does **not** include `package.json`, `package-lock.json`, `node_modules` or Next.js configuration files. Keep those from your installation.

## Before extracting

1. Stop `npm run dev` with `Ctrl+C` or leave it running and reload after extraction.
2. If you already modified `frontend/src/app/page.tsx`, `globals.css` or `layout.tsx`, back them up first: this update replaces those files.
3. Create a backup or commit your existing work if you want to preserve your changes.

## Extract

In PowerShell, from `C:\project_city\city-main` (after downloading this ZIP into Downloads):

```powershell
$zip = Join-Path $HOME 'Downloads\city-main-dashboard-update.zip'
Expand-Archive -LiteralPath $zip -DestinationPath 'C:\project_city\city-main' -Force
cd C:\project_city\city-main\frontend
npm run dev
```

Visit `http://localhost:3000`. Links and demo booking flows should work.

## Git repository setup (root repo only)

```powershell
cd C:\project_city\city-main
Test-Path .\frontend\.git
```

If `True` and the nested repo has no commits you need, remove the nested `.git` folder (not the source code):

```powershell
Remove-Item -Recurse -Force .\frontend\.git
```

Then initialize at the root **if not already initialized**:

```powershell
git status
# If 'not a git repository':
git init
git branch -M main
```

If the GitHub remote is not configured, add it:

```powershell
git remote -v
git remote add origin https://github.com/kingzmenx23/CityMain.git
```

If origin exists, do **not** add it a second time. Commit and push:

```powershell
git add .
git status
git commit -m "Build City Main dashboard and demo booking pages"
git push -u origin main
```

If the remote has existing commits and Git rejects the push, fetch and reconcile; do **not** use `--force`.
