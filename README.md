# aiot-classwork-DIC-4

物聯網應用與資料分析（AIoT-DA）第 12 組的期末專題「重機旅遊規劃顧問（Moto Touring Copilot）」，把中文課程 Proposal 改寫成投稿 ICEIB 2027 的英文會議論文（IEEE 格式，4–8 頁，2027-03-01 交摘要）。

## 目錄

| 資料夾 | 內容 |
| --- | --- |
| [`ICEIB2027-IEEE/`](ICEIB2027-IEEE/) | 英文論文的 LaTeX 原稿（IEEEtran `[conference]`，用 pdfLaTeX 在 Overleaf 編譯）。上傳方式、各章節進度與注意事項見 [ICEIB2027-IEEE/README.md](ICEIB2027-IEEE/README.md) |
| [`dic3-參考資料/`](dic3-參考資料/) | 寫論文用的原始資料：課程講義與作業規範、DIC-3 的交付稿、中文 Proposal 原稿 |

## 原始資料

### 課程資料與 DIC-3 交付稿

從 `aiot-classwork-DIC-3` 複製：

| 檔案 | 用途 |
| --- | --- |
| [`_AIoT_-DA_L16_打造_AGENT_(目標系統架構PDAC)OVERLEAF.pdf`](dic3-參考資料/_AIoT_-DA_L16_打造_AGENT_(目標系統架構PDAC)OVERLEAF.pdf) | L16 講義：ICEIB 2027 要求（英文、4–8 頁、2027-03-01 交摘要）與本專案結構 |
| [`期末專題提案作業規範.pdf`](dic3-參考資料/期末專題提案作業規範.pdf) | 課程作業規範（A–F、Related Work 表格、①–⑧ 架構、不得捏造結果） |
| [`delivery/03-ieee-abstract-en.md`](dic3-參考資料/delivery/03-ieee-abstract-en.md) | `00_abstract.tex` 的來源 |
| [`delivery/01-a-to-f-revision.md`](dic3-參考資料/delivery/01-a-to-f-revision.md) | A–F 修正稿，文末列出查證後不採用的說法 |
| [`delivery/02-summary-300.md`](dic3-參考資料/delivery/02-summary-300.md) | 300 字中文摘要 |

### 中文 Proposal 原稿

從 `moto-touring-copilot/docs/proposal/source/` 複製到 `dic3-參考資料/proposal/`。論文各 `.tex` 檔開頭的註解有寫對應的檔案。

| 檔案 | 用途 |
| --- | --- |
| [`00-abstract.md`](dic3-參考資料/proposal/00-abstract.md) | 中文摘要 |
| [`01-introduction.md`](dic3-參考資料/proposal/01-introduction.md) | 緒論（A–F、證據查證表），`01_introduction.tex` 與 `references.bib` [I1]–[I21] 的來源 |
| [`02-related-work.md`](dic3-參考資料/proposal/02-related-work.md) | 相關研究與查證紀錄，`02_related_work.tex` 的翻譯來源（[1]–[19]） |
| [`03-deep-research.md`](dic3-參考資料/proposal/03-deep-research.md) | 深度研究：騎士的核心思維模式與查證紀錄 |
| [`04-proposed-scheme.md`](dic3-參考資料/proposal/04-proposed-scheme.md) | 系統設計（PA–PC、①–⑧ 架構），`03_proposed_scheme.tex` 的翻譯來源；4.11 節是 `04_experiments.tex` 的來源 |
| [`05-ai-usage.md`](dic3-參考資料/proposal/05-ai-usage.md) | 附錄 A：AI 使用說明 |
| [`ai-usage-log.md`](dic3-參考資料/proposal/ai-usage-log.md) | AI 使用紀錄（提示詞摘要） |
| [`slides.md`](dic3-參考資料/proposal/slides.md) | 提案簡報內容與逐字稿 |
| [`metadata.yaml`](dic3-參考資料/proposal/metadata.yaml) | 中文 Proposal 的標題、作者與日期 |
| [`figures/fig1.mmd`](dic3-參考資料/proposal/figures/fig1.mmd) | ①–⑧ 系統架構圖（Mermaid，中文標籤），重畫論文的 `figures/architecture.pdf` 時參考 |
| [`figures/fig2.mmd`](dic3-參考資料/proposal/figures/fig2.mmd)、[`fig2.png`](dic3-參考資料/proposal/figures/fig2.png) | 規劃流程圖（Mermaid 原稿與輸出圖，中文標籤） |
