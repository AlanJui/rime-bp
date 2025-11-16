# GitHub Actions 自動建置與發行說明

## 概述

本專案的 GitHub Actions workflow 已更新，現在能夠自動建置 Windows 安裝程式並打包發行。

## Workflow 架構

### 三個主要 Job

```Bash
build-windows-installer (Windows)
         ↓
    [產生 installer.zip]
         ↓
         ├─→ create-release (Ubuntu)
         ↓
build-bundles (Ubuntu)
         ↓
    [產生 YAML bundles]
         ↓
         └─→ create-release (Ubuntu)
                  ↓
            [發布 Release]
```

### 1. build-windows-installer

**執行環境**: Windows Latest

**主要任務**:

- 檢出程式碼
- 設定 Python 3.11 環境
- 安裝 PyInstaller
- 執行 `tools/build_installer.py` 建置安裝程式
- 打包 `release/installer_package` 為 ZIP 檔
- 生成 SHA256 校驗碼
- 上傳為 artifact

**輸出檔案**:

- `rime-bp-installer-{TAG}.zip`
- `rime-bp-installer-{TAG}.zip.sha256`

### 2. build-bundles

**執行環境**: Ubuntu Latest

**主要任務**:

- 根據 `release-include.txt` 打包 YAML 配置檔
- 產生四個不同的方案包：
  - **ALL**: 完整版（所有方案）
  - **TLPA**: 台羅拼音方案
  - **ZU2**: 注音二式方案
  - **BP**: 閩拼方案
- 生成 SHA256 校驗碼
- 上傳為 artifact

**輸出檔案**:

- `rime-tlpa-all-{TAG}.zip`
- `rime-tlpa-tlpa-{TAG}.zip`
- `rime-tlpa-zu2-{TAG}.zip`
- `rime-tlpa-bp-{TAG}.zip`
- 對應的 `.sha256` 檔案

### 3. create-release

**執行環境**: Ubuntu Latest

**主要任務**:

- 等待前兩個 job 完成
- 下載所有 artifacts
- 合併所有檔案
- 建立 GitHub Release
- 上傳所有 ZIP 檔案和校驗碼

## 觸發方式

### 1. 自動觸發（推薦）

推送帶有版本標籤的 commit：

```bash
# 建立並推送版本標籤
git tag v1.0.0
git push origin v1.0.0

# 或使用其他前綴
git tag bp-1.0.0
git push origin bp-1.0.0
```

支援的標籤格式：

- `v*` - 通用版本（如 v1.0.0）
- `bp-*` - 閩拼專用版本
- `zu-*` - 注音二式專用版本
- `kb-*` - 鍵盤練習工具版本

### 2. 手動觸發

在 GitHub 網頁介面：

1. 進入 **Actions** 頁面
2. 選擇 **Build & Release YAML bundles** workflow
3. 點擊 **Run workflow**
4. 填寫參數：
   - **Branch 或 commit**: 選擇要建置的分支（預設 main）
   - **Release tag**: 輸入版本號（如 v1.0.0）
   - **是否標示為 pre-release**: 勾選表示這是預發行版本

## Release 內容

每次發行會包含以下檔案：

### Windows 安裝程式

- `rime-bp-installer-{TAG}.zip` - Windows 一鍵安裝包
- 包含 `rime_installer.exe`
- 包含所有必要的 RIME 配置檔案
- 包含 config 目錄
- 包含安裝說明

### YAML 配置包（手動安裝用）

- `rime-tlpa-all-{TAG}.zip` - 完整版
- `rime-tlpa-tlpa-{TAG}.zip` - TLPA 方案
- `rime-tlpa-zu2-{TAG}.zip` - 注音二式方案
- `rime-tlpa-bp-{TAG}.zip` - 閩拼方案

### 校驗碼

每個 ZIP 檔都附帶 `.sha256` 校驗檔案

## 使用者安裝流程

### 方法一：使用 Windows 安裝程式（推薦）

1. 從 Release 頁面下載 `rime-bp-installer-{版本}.zip`
2. 解壓縮到任意位置
3. 雙擊執行 `rime_installer.exe`
4. 按照程式指示完成安裝
5. 重新部署 RIME

**優點**：

- ✅ 自動備份現有配置
- ✅ 一鍵完成安裝
- ✅ 無需手動複製檔案
- ✅ 適合所有使用者

### 方法二：手動安裝 YAML 配置

1. 從 Release 頁面下載對應的方案 ZIP 檔
2. 解壓縮到 RIME 配置目錄：`%APPDATA%\Rime`
3. 手動重新部署 RIME

**適用情境**：

- 進階使用者
- 需要自訂配置
- Linux/macOS 使用者

## 開發流程

### 準備發行新版本

1. **確認所有變更已提交**

   ```bash
   git status
   git add .
   git commit -m "Prepare for release v1.0.0"
   ```

2. **更新版本號**（如果有 version_info.txt）

   ```bash
   echo "v1.0.0" > version_info.txt
   git commit -am "Bump version to v1.0.0"
   ```

3. **推送到 GitHub**

   ```bash
   git push origin main
   ```

4. **建立並推送版本標籤**

   ```bash
   git tag v1.0.0
   git push origin v1.0.0
   ```

5. **等待 GitHub Actions 完成**

   - 進入 GitHub Actions 頁面查看進度
   - 通常需要 5-10 分鐘

6. **檢查 Release**

   - 進入 Releases 頁面
   - 確認所有檔案都已上傳
   - 測試下載連結

### 發行預覽版本

如果要發行預覽版本（pre-release）：

```bash
git tag v1.0.0-beta.1
git push origin v1.0.0-beta.1
```

或使用手動觸發並勾選 "是否標示為 pre-release"

## 故障排除

### 建置失敗

1. **檢查 Actions 日誌**

   - 進入 GitHub Actions 頁面
   - 點擊失敗的 workflow
   - 查看詳細錯誤訊息

2. **常見問題**：

   - `build_installer.py` 找不到檔案
     - 確認 `release-include.txt` 中列出的檔案都存在
   - PyInstaller 建置失敗
     - 檢查 `rime_installer.py` 語法錯誤
   - 上傳 artifact 失敗
     - 確認檔案路徑正確

### Release 檔案缺失

如果某些檔案沒有出現在 Release 中：

1. 檢查對應的 job 是否成功完成
2. 確認 artifact 是否正確上傳
3. 檢查 `create-release` job 的日誌

### 手動重試

如果需要重新建置：

1. 刪除失敗的 Release
2. 刪除對應的 tag：

   ```bash
   git tag -d v1.0.0
   git push origin :refs/tags/v1.0.0
   ```

3. 重新建立並推送 tag

## 技術細節

### Workflow 相依性

```yaml
create-release:
  needs: [build-windows-installer, build-bundles]
```

`create-release` job 會等待前兩個 job 都成功完成後才執行。

### Artifact 傳遞

1. `build-windows-installer` 上傳 `windows-installer` artifact
2. `build-bundles` 上傳 `yaml-bundles` artifact
3. `create-release` 下載所有 artifacts 並合併

### 平台考量

- **Windows job**: 必須在 Windows 環境建置，因為 PyInstaller 打包的執行檔是平台相依的
- **Ubuntu jobs**: 用於 YAML 打包和 Release 建立，較快且成本較低

## 最佳實務

### 版本號命名

建議遵循語義化版本（Semantic Versioning）：

- **主版本號.次版本號.修訂號** (如 `v1.2.3`)
- **主版本號**: 不相容的 API 修改
- **次版本號**: 向下相容的功能新增
- **修訂號**: 向下相容的問題修正

範例：

- `v1.0.0` - 首次正式發行
- `v1.1.0` - 新增功能
- `v1.1.1` - 錯誤修正
- `v2.0.0` - 重大更新

### 發行前檢查清單

- [ ] 所有測試通過
- [ ] 文檔已更新
- [ ] CHANGELOG 已記錄變更
- [ ] 版本號已更新
- [ ] 本地測試 `build_installer.py` 成功
- [ ] commit 訊息清晰
- [ ] 準備好 Release Notes

### 安全性

- GitHub Actions 使用 `GITHUB_TOKEN` 自動授權
- 權限設定為 `contents: write` 以允許建立 Release
- 所有檔案都包含 SHA256 校驗碼供使用者驗證

## 相關檔案

- `.github/workflows/release-yamls.yml` - Workflow 定義
- `tools/build_installer.py` - 安裝程式建置腳本
- `tools/rime_installer.py` - 安裝程式主程式
- `release-include.txt` - 要打包的檔案清單

---

最後更新：2025-11-16
