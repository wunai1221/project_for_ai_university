# AI 客服系統

以 FastAPI + Ollama 本地模型為核心的客服對話系統，透過對話自動蒐集客戶資訊並輸出成 Word 表單。

---

## 環境需求

- Python 3.10+
- [Ollama](https://ollama.com/download) 已安裝並在本機執行

---

## 快速開始

### 1. 下載模型

確認 Ollama 已啟動後，下載模型：

```powershell  
ollama pull gemma4-E4b-it-uncensored

2. 安裝相依套件
pip install -r requirements.txt

3. 設定環境變數
複製範例檔並修改.env檔案

4. 啟動服務
python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
服務啟動後開啟：http://127.0.0.1:8000/docs