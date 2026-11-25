# DIC4 交接：用 MCP 修改 Overleaf 上的 IEEE 會議論文

## 作業要交什麼

- **期限**：2026-11-25，不收遲交，占成績 5%。
- **上傳 2 個 PDF**：
  1. 修改前的論文 PDF
  2. **透過 MCP** 修改後、在 Overleaf 重新編譯的 PDF
- **說明欄要寫**：GitHub repo 連結、Overleaf 唯讀連結，再加一段 **Review**，說明用 MCP 改了什麼、怎麼確認改對了。

## 事前準備

- 一個新的 GitHub repo（DIC-4 用），設成**公開**。
- Overleaf 帳號，免費版就可以。
- Node.js 20 以上，在終端機執行 `node --version` 確認。
- 已經裝好 Codex CLI。

## 步驟

### 0. 準備來源資料（從 DIC-3 的 GitHub 拿）

DIC4 的論文不是從頭開始寫，而是把 **DIC-3 的成果**改寫成英文 IEEE 論文。先把 DIC-3 的這些檔案複製到 DIC-4 repo 的 `dic3-參考資料/` 資料夾：

| 從 DIC-3 拿什麼 | 用在論文哪裡 |
| --- | --- |
| A–F 修正稿（`2-3_A-F修正稿.md`） | Introduction |
| 300 字中文摘要（`2-4_最後擷取重要文字_300字.md`） | 參考用 |
| IEEE Abstract（`3-1_IEEE_Transactions_Abstract.md`） | `00_abstract.tex` |
| 中文 Proposal 原稿（Introduction、Related Work、Proposed Scheme） | 各章節翻譯的來源 |
| 課程講義 L16（Overleaf 模板說明）、期末專題提案作業規範 PDF | 格式要求、評分標準 |

參考範例：

- **DIC-3 原始資料**：<https://github.com/yotsubamomo/aiot-classwork-DIC-3> 。DIC-3 的交付稿在 `docs/delivery/` 裡。
- **整理好的 DIC-4**：<https://github.com/yotsubamomo/aiot-classwork-DIC-4> 。`dic3-參考資料/` 是整理後的樣子，根目錄的 README 有一張表，寫出每個檔案對應論文的哪一部分。

可以直接叫 Codex 做：

> 把 `<自己的 DIC-3 repo 路徑>/docs/delivery/` 裡的 A–F 修正稿、300 字摘要、IEEE Abstract，還有中文 Proposal 原稿，複製到這個 repo 的 `dic3-參考資料/`。在根目錄 README 加一張表，說明每個檔案對應論文的哪一部分，然後 commit 並 push。

> ⚠️ 要用的是**自己組**的 DIC-3 成果。我們組的檔案只能當格式參考，不能拿來當你的論文內容。

### 1. 建立論文並放上 Overleaf

- 用老師 L16 講義裡的 `ICEIB2027-IEEE.zip` 模板（IEEE 雙欄，每個章節一個 `.tex` 檔）。
- 叫 Codex 把 `dic3-參考資料/` 的內容翻成英文，填進各章節的 `.tex` 檔。
- Overleaf → **New Project** → **Upload Project** → 上傳 zip。
- 確認編譯器是 **pdfLaTeX**：左下角齒輪 → Compiler。
- 論文原始碼也放進 GitHub repo，commit 並 push。

### 2. 不要用 Overleaf 內建的 Git

免費帳號 `git clone` 會出現 `no git access`，因為 Git 功能要專案擁有者付費才有。所以改用 MCP，免費版也能用。

### 3. 安裝 overleaf-web-mcp

```powershell
npx overleaf-web-mcp@1.4.1 login
```

執行後會開一個瀏覽器視窗，在裡面登入 Overleaf。接著把它加進 Codex：

```powershell
codex mcp add overleaf -- npx overleaf-web-mcp@1.4.1 serve
```

最後執行 `codex mcp list`，**確認清單裡有 overleaf**。如果沒有，重新執行一次 `codex mcp add`。確認後重開 Codex。

### 4. 先下載「修改前」的 PDF

在 Overleaf 網頁上按 **Recompile**，再按下載 PDF，存成 `DIC4-1-before-MCP-edit.pdf`。

### 5. 叫 Codex 透過 MCP 修改

專案 ID 就是 Overleaf 網址 `overleaf.com/project/` 後面那串。可以直接這樣跟 Codex 說：

> 用 overleaf MCP 讀取專案 `<專案ID>` 的 `main.tex`，把作者欄的 TODO 換成我的系所和學校名稱。寫入後在 Overleaf 上編譯，告訴我有沒有錯誤，再把 PDF 下載成 `DIC4-2-after-MCP-edit.pdf`。

要改什麼可以自己決定，改一個小地方就夠了。重點是修改、編譯、下載這三步都要**透過 MCP** 完成。

### 6. 同步到 GitHub

把同樣的修改套用到 repo 裡的 `.tex` 檔，再 commit 並 push。也可以叫 Codex 做。

### 7. 取得 Overleaf 唯讀連結

Overleaf 右上角 **Share** → 打開 **Link sharing** → 複製 **View only** 的連結。用無痕視窗打開一次，確認不能編輯。

### 8. 交作業

上傳兩個 PDF，說明欄貼上 GitHub 連結、Overleaf 連結，再加一段 Review。Review 可以照這個格式寫：

- **工具**：overleaf-web-mcp
- **修改內容**：改了哪個檔案的哪個地方
- **流程**：用 MCP 讀取檔案 → 寫入修改（有版本檢查，不會蓋掉別人的修改）→ 在 Overleaf 編譯 → 下載 PDF
- **檢查結果**：修改前後都編譯成功、0 個錯誤；比對兩份 PDF，只有修改的地方不同；同樣的修改已經同步到 GitHub

## 常見問題

- **圖片顯示成外框佔位**：圖片的資料夾放錯位置了。`figures/` 要放在專案最外層，跟 `main.tex` 同一層，不能放在 `sections/` 裡面。
- **個人資料**：PDF 裡如果有 email，GitHub 又是公開的，上傳前想清楚要不要放。
- **用完記得清除登入**：MCP 保存了你的 Overleaf 登入，可以操作你整個帳號。作業交完後執行 `codex mcp remove overleaf`，再到 Overleaf 帳號設定裡登出所有裝置。
