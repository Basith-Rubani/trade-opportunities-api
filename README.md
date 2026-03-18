# 📊 Trade Opportunities API

## 🚀 Overview

The Trade Opportunities API is a FastAPI-based service that analyzes market news data for specific sectors in India and generates structured trade opportunity insights.

The API collects current market information, processes it using an AI model, and returns a **markdown-formatted report** highlighting:

- Trends 📈
- Opportunities 💡
- Risks ⚠️

---

## 🧱 Tech Stack

- **Backend**: FastAPI
- **AI Model**: OpenRouter (LLM - GPT-3.5 Turbo)
- **Data Source**: Market news (mock / API-based)
- **Language**: Python
- **Other Tools**:
  - dotenv (environment variables)
  - requests (API calls)
  - slowapi (rate limiting)

---

## ⚙️ Features

### ✅ Core Functionality

- Analyze market sectors dynamically
- Fetch relevant news data
- Generate AI-based insights
- Return structured markdown reports

### 🔐 Security

- API Key Authentication
- Input validation
- Rate limiting (5 requests/minute per user)

### ⚡ Reliability

- Fallback analysis if AI fails
- Error handling for external APIs

---

## 📡 API Endpoint

### 🔹 GET `/analyze/{sector}`

#### Example:

GET /analyze/technology

#### Headers:

x-api-key: mysecurekey123

---

## 📄 Response Format

```json
{
  "sector": "technology",
  "message": "Report saved as technology_report.md",
  "report_markdown": "## Trends\n- ...",
  "report_lines": [
    "## Trends",
    "- ..."
  ]
}
📝 Output

The API generates a .md (Markdown) file for each request

Example:

technology_report.md
Sample Markdown Output:
## Trends
- Market growth observed
- Increasing digitization

## Opportunities
- AI adoption rising
- Investment potential increasing

## Risks
- Competition from global markets
- Regulatory challenges



🧪 How to Run

1️⃣ Clone Project
git clone <your-repo-link>
cd trade_api
2️⃣ Create Virtual Environment
python -m venv venv
venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Setup Environment Variables

Create .env file:

OPENROUTER_API_KEY=your_api_key_here

5️⃣ Run Server
uvicorn main:app --reload
🌐 Testing the API
🔹 Swagger UI (Recommended)
http://127.0.0.1:8000/docs
🔹 ReDoc
http://127.0.0.1:8000/redoc
🔹 cURL Example
curl -H "x-api-key: mysecurekey123" http://127.0.0.1:8000/analyze/technology


🤖 AI Integration

Initially designed to use Google Gemini API

Due to quota limitations, switched to OpenRouter (GPT-3.5 Turbo)

🔁 Fallback Mechanism

If AI API fails:

A rule-based analysis system generates insights

Ensures uninterrupted service

🧠 Design Decisions

Modular architecture:

data_collector → fetch data

ai_service → process insights

main → API layer

Reduced token usage for efficiency

Markdown format for better readability and export

⚠️ Limitations

Uses limited news samples (for free-tier optimization)

No database (in-memory only as per requirement)

📌 Future Improvements

Add real-time news APIs

Enhance AI prompt engineering

Add user authentication with JWT

Store historical reports

👨‍💻 Author

Basith Rubani

✅ Conclusion

This project demonstrates:

FastAPI backend development

AI integration with fallback handling

Secure and scalable API design

Clean, production-ready architecture
```
