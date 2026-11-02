# 🔎 End-to-End Multi-Agent AI Research System

A multi-agent AI pipeline that **searches the web, scrapes content, writes a research report, and critiques it** — all automatically. Built with LangChain, Google Gemini, Tavily, and Streamlit.

---

## 🧠 How It Works

Four specialized agents collaborate in a sequential pipeline:

```
Topic Input
    │
    ▼
┌─────────────────────┐
│  Agent 1 · Search   │  Tavily web search → top 5 results
└─────────────────────┘
    │
    ▼
┌─────────────────────┐
│  Agent 2 · Reader   │  Scrapes the top URL for deeper content
└─────────────────────┘
    │
    ▼
┌─────────────────────┐
│  Chain 3 · Writer   │  Gemini drafts a structured research report
└─────────────────────┘
    │
    ▼
┌─────────────────────┐
│  Chain 4 · Critic   │  Gemini scores and reviews the report
└─────────────────────┘
    │
    ▼
 Final Report + Feedback
```

---

## 📁 Project Structure

```
End-to-End Multi-Agent AI System/
│
├── app.py                        # Streamlit UI
├── requirements.txt
├── .env                          # API keys (not committed)
│
└── src/
    ├── tools/
    │   └── tools.py              # web_search & scrape_url tools
    ├── agents/
    │   └── agents.py             # Agent & chain definitions
    └── pipeline/
        └── pipeline.py           # Orchestrates all 4 steps
```

---

## ⚙️ Setup

### 1. Clone the repo

```bash
git clone <your-repo-url>
cd "End-to-End Multi-Agent AI System"
```

### 2. Create a virtual environment

```bash
python -m venv .venv
.venv\Scripts\activate        # Windows
# source .venv/bin/activate   # macOS / Linux
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure API keys

Create a `.env` file in the project root:

```env
TAVILY_API_KEY=your_tavily_api_key_here
GOOGLE_API_KEY=your_google_api_key_here
```

| Key | Where to get it |
|-----|----------------|
| `TAVILY_API_KEY` | [app.tavily.com](https://app.tavily.com) |
| `GOOGLE_API_KEY` | [aistudio.google.com/apikey](https://aistudio.google.com/apikey) |

---

## 🚀 Run the App

```bash
$env:PYTHONIOENCODING="utf-8"   # Windows (prevents emoji encoding errors)
python -m streamlit run app.py
```

Then open [http://localhost:8501](http://localhost:8501) in your browser.

---

## 🖥️ UI Overview

1. Enter a research topic in the text input
2. Click **Run research pipeline**
3. Watch the 4 agents work in real time
4. View search results, scraped content, the full report, and critic feedback
5. Download the report as a `.md` file

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|-----------|
| LLM | Google Gemini 3.8 Flash (`gemini-3.8-flash`) |
| Web Search | Tavily Search API |
| Web Scraping | `requests` + `BeautifulSoup4` |
| Agent Framework | LangChain + LangGraph |
| UI | Streamlit |
| Output Formatting | Rich |

---

## 📦 Dependencies

```
langchain
langchain-google-genai
langgraph
tavily-python
python-dotenv
requests
beautifulsoup4
rich
streamlit
```

---

## ⚠️ Notes

- Some websites (e.g. Medium) block scrapers — the reader agent handles this gracefully and the writer continues with search results alone.
- Set `PYTHONIOENCODING=utf-8` before running on Windows to avoid emoji encoding errors in the terminal.
- The Gemini model must be run with **network access** — do not run inside an isolated/sandboxed environment.

