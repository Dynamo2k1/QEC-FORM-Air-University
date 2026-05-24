## QEC Auto-Filler v2.0.0

### Download

| OS | File |
|---|---|
| 🪟 Windows | `QEC-AutoFiller-Windows.exe` |
| 🐧 Linux | `QEC-AutoFiller-Linux` |

### How to Use

**Windows:** Download `QEC-AutoFiller-Windows.exe` → double-click → enter credentials → done.

**Linux:**
```bash
chmod +x QEC-AutoFiller-Linux
./QEC-AutoFiller-Linux
```

**Requirement:** Google Chrome or Chromium must be installed on your machine.
On first run it auto-downloads ChromeDriver (~6 MB). After that it's instant.

### What's New in v2.0.0

- Standalone binaries — no Python install needed
- Auto ChromeDriver download on first run
- Headless mode (no browser window)
- Login error detection
- Cleaner terminal output with step progress
- Windows Defender note: click "More info" → "Run anyway" if a warning appears (unsigned EXE false positive)

### Source Code

Want to build yourself or customize? Clone the repo and run `build_windows.bat` (Windows) or `build_linux.sh` (Linux). Full instructions in README.
