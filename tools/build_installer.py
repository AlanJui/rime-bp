#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
RIME 安裝程式打包工具
使用 PyInstaller 將 rime_installer.py 打包成獨立的 .exe 執行檔
"""

import os
import shutil
import subprocess
import sys
from pathlib import Path


def safe_print(text):
    """編碼安全的 print 函數，避免在不支援 UTF-8 的環境中出錯"""
    try:
        print(text)
    except UnicodeEncodeError:
        # 移除無法編碼的字元後重試
        print(text.encode('ascii', 'ignore').decode('ascii'))
    except Exception:
        # 最後的備援方案
        pass


def check_pyinstaller():
    """檢查 PyInstaller 是否已安裝"""
    try:
        import PyInstaller
        safe_print(f"✅ 找到 PyInstaller 版本: {PyInstaller.__version__}")
        return True
    except ImportError:
        safe_print("❌ PyInstaller 未安裝")
        return False


def install_pyinstaller():
    """安裝 PyInstaller"""
    safe_print("🔄 正在安裝 PyInstaller...")
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])
        safe_print("✅ PyInstaller 安裝成功")
        return True
    except subprocess.CalledProcessError as e:
        safe_print(f"❌ PyInstaller 安裝失敗: {e}")
        return False


def create_spec_file():
    """創建 PyInstaller 規格檔案"""
    # 檢測當前是否在 tools 目錄中
    current_dir = Path.cwd()
    is_in_tools = current_dir.name == 'tools'

    # 根據位置調整相對路徑
    if is_in_tools:
        # 在 tools 目錄中執行
        release_include_path = '../release-include.txt'
        rime_files_path = '../release/rime_files'
        config_path = '../config'
        icon_path = '../assets/icon.ico'
    else:
        # 在項目根目錄執行
        release_include_path = 'release-include.txt'
        rime_files_path = 'release/rime_files'
        config_path = 'config'
        icon_path = 'assets/icon.ico'

    # 檢查圖示檔案是否存在
    icon_exists = Path(icon_path).exists()
    icon_line = f"    icon='{icon_path}'," if icon_exists else "    icon=None,"

    # 使用字串組合而不是 f-string 來避免複雜的轉義問題
    # 注意：我們不在這裡打包資源檔案，而是讓執行檔從執行檔目錄讀取
    spec_content = """# -*- mode: python ; coding: utf-8 -*-

block_cipher = None

a = Analysis(
    ['rime_installer.py'],
    pathex=[],
    binaries=[],
    datas=[],
    hiddenimports=[],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.zipfiles,
    a.datas,
    [],
    name='rime_installer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    upx_exclude=[],
    runtime_tmpdir=None,
    console=True,
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
""" + icon_line + """
)
"""

    spec_file = Path('rime_installer.spec')
    with open(spec_file, 'w', encoding='utf-8') as f:
        f.write(spec_content)

    safe_print(f"✅ 已創建規格檔案: {spec_file}")
    return spec_file


def build_executable():
    """使用 PyInstaller 打包執行檔"""
    safe_print("🔄 開始打包執行檔...")

    # 創建規格檔案
    spec_file = create_spec_file()

    try:
        # 執行 PyInstaller
        cmd = [
            sys.executable, "-m", "PyInstaller",
            "--clean",
            "--noconfirm",
            str(spec_file)
        ]

        safe_print(f"執行命令: {' '.join(cmd)}")
        result = subprocess.run(cmd, check=True, capture_output=True, text=True)

        safe_print("✅ 打包成功!")

        # 檢查輸出檔案
        dist_dir = Path("dist")
        exe_file = dist_dir / "rime_installer.exe"

        if exe_file.exists():
            file_size = exe_file.stat().st_size / (1024 * 1024)  # MB
            safe_print(f"📦 執行檔位置: {exe_file}")
            safe_print(f"📊 檔案大小: {file_size:.1f} MB")
            return exe_file
        else:
            safe_print("❌ 找不到輸出的執行檔")
            return None

    except subprocess.CalledProcessError as e:
        safe_print(f"❌ 打包失敗: {e}")
        if e.stdout:
            safe_print("標準輸出:" + e.stdout)
        if e.stderr:
            safe_print("錯誤輸出:" + e.stderr)
        return None


def create_installer_package():
    """創建完整的安裝包"""
    safe_print("📦 創建安裝包...")

    # 檢測當前是否在 tools 目錄中
    current_dir = Path.cwd()
    is_in_tools = current_dir.name == 'tools'

    # 根據位置調整相對路徑
    if is_in_tools:
        package_dir = Path("../release/installer_package")
    else:
        package_dir = Path("release/installer_package")

    package_dir.mkdir(parents=True, exist_ok=True)

    # 複製執行檔
    exe_file = Path("dist/rime_installer.exe")
    if exe_file.exists():
        shutil.copy2(exe_file, package_dir / "rime_installer.exe")
        safe_print(f"✅ 已複製執行檔到: {package_dir}")

    # 複製必要檔案
    if is_in_tools:
        files_to_copy = [
            ("../release-include.txt", "release-include.txt"),
            ("../README.md", "README.md"),
        ]
    else:
        files_to_copy = [
            ("release-include.txt", "release-include.txt"),
            ("README.md", "README.md"),
        ]

    for src, dst in files_to_copy:
        src_path = Path(src)
        if src_path.exists():
            shutil.copy2(src_path, package_dir / dst)
            safe_print(f"✅ 已複製: {dst}")

    # 創建 rime_files 目錄並根據 release-include.txt 複製檔案
    rime_files_dst = package_dir / "rime_files"
    rime_files_dst.mkdir(exist_ok=True)

    # 讀取 release-include.txt 並複製指定檔案
    if is_in_tools:
        release_include_path = Path("../release-include.txt")
        project_root = Path("..")
    else:
        release_include_path = Path("release-include.txt")
        project_root = Path(".")

    if release_include_path.exists():
        copied_count = 0
        with open(release_include_path, 'r', encoding='utf-8') as f:
            for line in f:
                line = line.strip()
                # 跳過註解和空行
                if line and not line.startswith('#'):
                    src_file = project_root / line
                    if src_file.exists():
                        dst_file = rime_files_dst / line
                        # 確保目標目錄存在
                        dst_file.parent.mkdir(parents=True, exist_ok=True)
                        shutil.copy2(src_file, dst_file)
                        copied_count += 1
        safe_print(f"✅ 已複製 {copied_count} 個 RIME 檔案到 rime_files 目錄")

    # 複製 config 目錄
    if is_in_tools:
        config_src = Path("../config")
    else:
        config_src = Path("config")

    if config_src.exists():
        config_dst = package_dir / "config"
        if config_dst.exists():
            shutil.rmtree(config_dst)
        shutil.copytree(config_src, config_dst)
        safe_print("✅ 已複製: config 目錄")

    # 創建使用說明
    readme_content = """# RIME 閩拚輸入法安裝程式

## 使用方法

1. 請先確認已安裝 RIME 小狼毫輸入法
   - 下載網址: https://rime.im/

2. 雙擊 `rime_installer.exe` 執行安裝程式

3. 按照程式指示完成安裝

4. 安裝完成後，請重新部署 RIME：
   - 右鍵點擊系統匣中的 RIME 圖示
   - 選擇「重新部署」
   - 等待部署完成

## 注意事項

- 安裝程式會自動備份現有的配置檔案
- 如有問題，請檢查備份檔案
- 建議在安裝前關閉正在使用的輸入法程式

## 檔案說明

- `rime_installer.exe`: 主要安裝程式
- `rime_files/`: RIME 配置檔案
- `config/`: 額外配置檔案
- `release-include.txt`: 檔案清單

---
閩拚輸入法專案
"""

    with open(package_dir / "安裝說明.txt", 'w', encoding='utf-8') as f:
        f.write(readme_content)

    safe_print(f"✅ 安裝包創建完成: {package_dir}")
    return package_dir


def clean_build_files():
    """清理建置檔案"""
    safe_print("🧹 清理建置檔案...")

    dirs_to_clean = ["build", "dist", "__pycache__"]
    files_to_clean = ["*.spec"]

    for dir_name in dirs_to_clean:
        dir_path = Path(dir_name)
        if dir_path.exists():
            shutil.rmtree(dir_path)
            safe_print(f"✅ 已刪除: {dir_name}")

    for pattern in files_to_clean:
        for file_path in Path(".").glob(pattern):
            file_path.unlink()
            safe_print(f"✅ 已刪除: {file_path}")


def main():
    """主函式"""
    safe_print("=" * 60)
    safe_print("🚀 RIME 閩拚輸入法安裝程式打包工具")
    safe_print("=" * 60)

    # 智能檢測項目結構和工作目錄
    current_dir = Path.cwd()
    script_dir = Path(__file__).parent

    # 可能的 rime_installer.py 位置
    possible_locations = [
        current_dir / "tools" / "rime_installer.py",  # 在項目根目錄執行
        script_dir / "rime_installer.py",             # 在 tools 目錄執行
        current_dir / "rime_installer.py"              # 直接在當前目錄
    ]

    rime_installer_path = None
    working_dir = None

    for path in possible_locations:
        if path.exists():
            rime_installer_path = path
            working_dir = path.parent
            break

    if not rime_installer_path:
        safe_print("❌ 找不到 rime_installer.py，請檢查檔案是否存在")
        safe_print("   已檢查位置:")
        for path in possible_locations:
            safe_print(f"   - {path}")
        return False

    safe_print(f"✅ 找到 rime_installer.py: {rime_installer_path}")
    safe_print(f"📍 工作目錄: {working_dir}")

    # 切換到正確的工作目錄
    original_cwd = Path.cwd()
    os.chdir(working_dir)
    safe_print(f"🔄 已切換工作目錄到: {Path.cwd()}")

    # 檢查並安裝 PyInstaller
    if not check_pyinstaller():
        if not install_pyinstaller():
            safe_print("❌ 無法安裝 PyInstaller，請手動安裝")
            return False

    try:
        # 清理舊的建置檔案
        clean_build_files()

        # 打包執行檔
        exe_file = build_executable()
        if not exe_file:
            safe_print("❌ 打包失敗")
            return False

        # 創建安裝包
        package_dir = create_installer_package()

        safe_print("\n" + "=" * 60)
        safe_print("🎉 打包完成!")
        safe_print("=" * 60)
        safe_print(f"📦 安裝包位置: {package_dir}")
        safe_print(f"🎯 執行檔位置: {exe_file}")
        safe_print("\n📝 後續步驟:")
        safe_print("1. 測試執行檔是否正常運作")
        safe_print("2. 將安裝包分發給使用者")
        safe_print("3. 提供安裝說明文件")

        return True

    except Exception as e:
        safe_print(f"❌ 打包過程中發生錯誤: {e}")
        return False
    finally:
        # 恢復原始工作目錄
        os.chdir(original_cwd)
        safe_print(f"🔄 已恢復工作目錄到: {Path.cwd()}")
        # 可選：保留或清理建置檔案
        # clean_build_files()
        pass


if __name__ == "__main__":
    success = main()
    # 只在互動式環境中等待使用者輸入
    if sys.stdin.isatty():
        input(f"\n{'✅ 打包成功!' if success else '❌ 打包失敗!'} 按 Enter 鍵結束...")
    sys.exit(0 if success else 1)