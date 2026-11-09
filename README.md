# AshClip 📎

A lightweight background daemon that fetches file content from **Nexus Hub** straight to your clipboard with a global hotkey (`Ctrl+Shift+A`).

---

## ✨ Features

- **Ghost mode** — runs headless in the background, no console window
- **Smart detection** — distinguishes public files (`filename.txt`) from private files (`1234/filename.txt`)
- **Global hotkeys** — `Ctrl+Shift+A` to fetch, `Ctrl+Z` to stop
- **Cross-platform** — Windows (native `CREATE_NO_WINDOW`), macOS/Linux
- **Configurable** — point to your own Nexus Hub instance via `.env`

---

## 🚀 Quick Install

```bash
pip install ashclip
```

Then run once to start the background listener:

```bash
ashclip
```

> You'll see: `AshClip is now running in ghost mode. You can close this terminal.`

---

## 🔧 Configuration

Create a `.env` file (or set the environment variable):

```bash
cp .env.example .env
# edit .env if your Nexus Hub runs elsewhere
```

| Variable | Default | Purpose |
|---|---|---|
| `NEXUS_HUB_URL` | `https://cmd.pythonanywhere.com` | Base URL of your Nexus Hub instance |

---

## 📋 Usage

1. Copy a filename to clipboard:
   - Public: `solution.txt`
   - Private: `1234/secret_notes.txt` (4-digit code + filename)

2. Press **`Ctrl+Shift+A`** — AshClip fetches the content and replaces your clipboard with the file contents.

3. Paste anywhere (`Ctrl+V`).

4. Stop the daemon anytime with **`Ctrl+Z`** (global kill switch).

---

## 🛠️ Development

```bash
git clone https://github.com/MasterHacx/ashclip.git
cd ashclip
pip install -e .
ashclip --background   # run directly for debugging
```

---

## 📦 Build & Publish (maintainers)

```bash
python -m build
twine upload dist/*
```

> **⚠️ Never commit `.env` or PyPI tokens.** The `asclip-token.txt` file in the old archive is a live token — rotate it on PyPI if it was ever exposed.

---

## 📄 License

MIT License — see `LICENSE` (add one if needed).

---

## 👤 Author

**MasterHacx** — [GitHub](https://github.com/MasterHacx) • [PyPI](https://pypi.org/project/ashclip/)
