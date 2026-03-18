import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("OPENROUTER_API_KEY")


def fallback_analysis(news):
    trends, opportunities, risks = [], [], []

    for item in news:
        text = (item.get("title", "") + " " + item.get("body", "")).lower()

        if "growth" in text:
            trends.append("Market growth observed")

        if "ai" in text or "technology" in text:
            trends.append("AI adoption increasing")

        if "startup" in text:
            opportunities.append("Startup ecosystem growing")

        if "investment" in text:
            opportunities.append("Investment opportunities rising")

        if "risk" in text or "decline" in text:
            risks.append("Potential market risks")

    return f"""
## Trends
{chr(10).join(['- ' + t for t in set(trends)])}

## Opportunities
{chr(10).join(['- ' + o for o in set(opportunities)])}

## Risks
{chr(10).join(['- ' + r for r in set(risks)])}
"""


def analyze_news(sector, news):
    if not news:
        return "No news available"

    limited_news = news[:2]

    prompt = f"""
Analyze this news for the {sector} sector:

{limited_news}

Generate a structured markdown report with:

## Trends
- ...

## Opportunities
- ...

## Risks
- ...
"""

    try:
        response = requests.post(
            "https://openrouter.ai/api/v1/chat/completions",
            headers={
                "Authorization": f"Bearer {API_KEY}",
                "Content-Type": "application/json"
            },
            json={
                "model": "openai/gpt-3.5-turbo",
                "messages": [
                    {"role": "user", "content": prompt}
                ]
            }
        )

        data = response.json()

        return data["choices"][0]["message"]["content"]

    except Exception as e:
        print("AI ERROR:", e)
        return fallback_analysis(news)