# Financial Research Agent using PhiData

A practical agentic AI application that fetches real-time financial data and news,
then summarizes analyst recommendations and recent developments for a given stock.

This project demonstrates how to build a **tool-augmented AI agent** using
[PhiData](https://github.com/phidatahq/phidata), without relying on closed-source APIs.

---

## 🚀 Features

- Fetches **analyst recommendations** using Yahoo Finance
- Retrieves **latest stock-related news** via DuckDuckGo search
- Uses an **agentic workflow** (reasoning + tools)
- Outputs results in **structured tables and summaries**
- Runs locally with **open-source LLMs** (via Ollama) or hosted models

---

## 🧠 Architecture Overview

The agent follows a simple but effective flow:

1. User asks a financial question (e.g., NVDA analysis)
2. Agent decides which tools to use
3. Tools fetch structured data (analyst ratings, news)
4. LLM synthesizes results into a readable summary

---

## 🛠️ Tech Stack

- **Python**
- **PhiData** – Agent framework
- **Yahoo Finance API** (via `yfinance`)
- **DuckDuckGo Search**
- **Ollama / OpenAI / Gemini** (model interchangeable)

---

## 📦 Installation

### 1️⃣ Clone the repository
```bash
git clone https://github.com/<your-username>/financial-agent-phidata.git
cd financial-agent-phidata
```
### 2️⃣ Create and activate a virtual environment
```bash
python -m venv venv
venv\Scripts\activate   # Windows
```
### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```
🔑 Environment Variables

Create a .env file in the project root:

OPENAI_API_KEY=your_api_key_here


If using Ollama, no API key is required.

### ▶️ Usage

Run the agent:
```bash
python financial_agent.py
```

### Example query:

Summarize analyst recommendations and share the latest news for NVDA

### 📌 Notes

This project focuses on practical agent design, not model fine-tuning

Multi-agent setups were intentionally avoided for reliability

Designed for learning, experimentation, and portfolio demonstration
