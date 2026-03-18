import feedparser
import urllib.parse

def fetch_market_news(sector: str):
    query = f"{sector} industry India news"
    encoded_query = urllib.parse.quote(query)

    url = f"https://news.google.com/rss/search?q={encoded_query}&hl=en-IN&gl=IN&ceid=IN:en"

    feed = feedparser.parse(url)

    results_list = []

    for entry in feed.entries[:5]:
        results_list.append({
            "title": entry.title,
            "body": clean_html(entry.summary) if hasattr(entry, "summary") else "",
            "link": entry.link
        })

    # fallback
    if not results_list:
        results_list = [
            {
                "title": f"{sector} sector growth trends",
                "body": f"The {sector} sector in India is experiencing growth and emerging opportunities.",
                "link": "N/A"
            }
        ]

    return results_list

def clean_html(raw_text):
    import re
    clean = re.sub('<.*?>', '', raw_text)
    clean = clean.replace("&nbsp;", " ")
    return clean