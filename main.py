from fastapi import FastAPI, HTTPException, Header, Request
from services.data_collector import fetch_market_news
from services.ai_service import analyze_news

from slowapi import Limiter
from slowapi.util import get_remote_address

app = FastAPI()

# Simple API Key for Auth
API_KEY = "mysecurekey123"

# Rate Limiter
limiter = Limiter(key_func=get_remote_address)
app.state.limiter = limiter


@app.get("/analyze/{sector}")
@limiter.limit("5/minute")
def analyze_sector(request: Request, sector: str, x_api_key: str = Header(None)):

    # Auth checking
    if x_api_key != API_KEY:
        raise HTTPException(status_code=401, detail="Unauthorized")

    # Input validation
    if not sector.isalpha():
        raise HTTPException(status_code=400, detail="Invalid sector name")

    # Fetching the news
    news = fetch_market_news(sector)

    # Analyzing the news
    analysis = analyze_news(sector, news)

    # Save as markdown file
    filename = f"{sector}_report.md"
    with open(filename, "w", encoding="utf-8") as f:
        f.write(analysis)

        return {
    "sector": sector,
    "message": f"Report saved as {filename}",
    "report": analysis.split("\n") 
}
    