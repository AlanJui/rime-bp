@echo off
chcp 65001 >nul
setlocal EnableDelayedExpansion

echo ==========================================
echo 🚀 RIME 閩拚輸入法完整建置與測試流程
echo ==========================================
echo.

cd /d "%~dp0"

:: 檢查 Python 環境
echo 🔍 檢查 Python 環境...
python --version >nul 2>&1
if %errorlevel% neq 0 (
    echo ❌ 找不到 Python，請先安裝 Python 3.6+ 版本
    echo    下載網址: https://www.python.org/downloads/
    pause
    exit /b 1
)

for /f "tokens=*" %%i in ('python --version') do set PYTHON_VERSION=%%i
echo ✅ 找到 !PYTHON_VERSION!
echo.

:: 步驟 1: 清理舊檔案
echo 📁 步驟 1: 清理舊的建置檔案...
if exist build rmdir /s /q build
if exist dist rmdir /s /q dist
if exist __pycache__ rmdir /s /q __pycache__
if exist *.spec del /q *.spec
echo ✅ 清理完成
echo.

:: 步驟 2: 執行打包
echo 📦 步驟 2: 開始打包安裝程式...
echo 執行: python build_installer.py
echo.
python build_installer.py
if %errorlevel% neq 0 (
    echo ❌ 打包失敗
    pause
    exit /b 1
)
echo.

:: 步驟 3: 執行測試
echo 🧪 步驟 3: 執行測試...
echo 執行: python test_installer.py
echo.
python test_installer.py
if %errorlevel% neq 0 (
    echo ⚠️ 測試過程中發現問題，請檢查報告
) else (
    echo ✅ 測試完成
)
echo.

:: 步驟 4: 顯示結果
echo 📊 步驟 4: 建置結果
echo ==========================================

set "PACKAGE_DIR=..\release\installer_package"
set "EXE_FILE=!PACKAGE_DIR!\rime_installer.exe"

if exist "!EXE_FILE!" (
    for %%F in ("!EXE_FILE!") do set "FILE_SIZE=%%~zF"
    set /a FILE_SIZE_MB=!FILE_SIZE! / 1048576
    echo ✅ 執行檔: !EXE_FILE!
    echo 📊 檔案大小: !FILE_SIZE_MB! MB

    if exist "!PACKAGE_DIR!" (
        echo ✅ 安裝包: !PACKAGE_DIR!

        :: 計算檔案數量
        set "FILE_COUNT=0"
        for /r "!PACKAGE_DIR!" %%f in (*) do set /a FILE_COUNT+=1
        echo 📁 包含檔案: !FILE_COUNT! 個
    )

    echo.
    echo 🎉 建置成功！
    echo.
    echo 📋 後續步驟:
    echo 1. 在目標環境測試執行檔
    echo 2. 確認所有功能正常運作
    echo 3. 準備分發給使用者
    echo 4. 提供安裝說明文件

) else (
    echo ❌ 建置失敗，找不到執行檔
    echo    預期位置: !EXE_FILE!
)

echo.
echo ==========================================
echo 📂 相關檔案:
echo ==========================================
echo 🔨 建置工具: build_installer.py
echo 🧪 測試工具: test_installer.py
echo 📖 說明文件: 打包說明.md
echo 📦 安裝包: !PACKAGE_DIR!
echo ==========================================

echo.
pause