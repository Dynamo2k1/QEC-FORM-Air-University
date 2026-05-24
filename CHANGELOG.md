# Changelog

All notable changes to QEC Auto-Filler are documented here.

---

## [v2.0.0] — 2026-05-25

### Added
- **Standalone binaries** — no Python or driver installation required for end users
- **Auto ChromeDriver download** — selenium-manager fetches the correct driver on first run
- **Headless mode** — no browser window pops up during form filling
- **Login error detection** — clear message if credentials are wrong instead of silent crash
- **Graceful exit** — "Press Enter to exit" so the window doesn't close instantly on Windows
- `build_windows.bat` — one-click Windows EXE builder
- `build_linux.sh` — one-click Linux binary builder
- `CHANGELOG.md` — this file

### Changed
- Rewrote credential prompt with cleaner UI (clear screen, banner, step labels)
- Improved alert handling — no crash if no alert appears
- Better error messages for Chrome not found

### Fixed
- Non-BMP character stripping for special comment text
- Scroll-and-retry logic for radio buttons hidden behind overlays

---

## [v1.0.0] — 2026-05-23

### Initial Release
- Selenium-based script to fill QEC forms automatically
- Covers Student Course Evaluation, Teacher Evaluation, Online Learning Feedback
- Marks all answers as A (Strongly Agree)
- Secure password prompt (not shown on screen, not saved)
