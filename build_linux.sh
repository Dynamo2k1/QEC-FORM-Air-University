#!/usr/bin/env bash
# ============================================================
# build_linux.sh — Build QEC-AutoFiller-Linux ELF binary
# ============================================================
set -e

echo ""
echo " ====================================================="
echo "  QEC Auto-Filler  |  Linux Binary Builder"
echo " ====================================================="
echo ""

# Check Python
if ! command -v python3 &>/dev/null; then
    echo " [ERROR] python3 not found."
    echo " Install: sudo apt install python3 python3-pip"
    exit 1
fi

echo " [1/3] Installing required packages..."
pip3 install pyinstaller selenium --quiet

echo " [2/3] Building binary with PyInstaller..."
pyinstaller \
    --onefile \
    --console \
    --name "QEC-AutoFiller-Linux" \
    --hidden-import selenium \
    --hidden-import selenium.webdriver \
    --hidden-import selenium.webdriver.chrome \
    --hidden-import selenium.webdriver.chrome.service \
    --hidden-import selenium.webdriver.support.ui \
    --hidden-import selenium.webdriver.support.expected_conditions \
    --hidden-import selenium.webdriver.common.by \
    --hidden-import selenium.webdriver.common.keys \
    --hidden-import selenium.common.exceptions \
    QEC-FORM.py

echo " [3/3] Done!"
echo ""
echo " ====================================================="
echo "  Binary ready at: dist/QEC-AutoFiller-Linux"
echo " ====================================================="
echo ""
echo " Run with:"
echo "   chmod +x dist/QEC-AutoFiller-Linux"
echo "   ./dist/QEC-AutoFiller-Linux"
echo ""
echo " Users only need Chrome/Chromium installed — nothing else."
echo ""
