import requests
from bs4 import BeautifulSoup
from datetime import datetime

def scrape_capterra(company, start_date, end_date):
    start_date = datetime.fromisoformat(start_date)
    end_date = datetime.fromisoformat(end_date)

    url = f"https://www.capterra.com/p/{company}/reviews/"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, "html.parser")

    reviews = []

    for r in soup.select(".review"):
        date_text = r.select_one(".review-date").text.strip()
        review_date = datetime.strptime(date_text, "%b %d, %Y")

        if start_date <= review_date <= end_date:
            reviews.append({
                "title": r.select_one("h3").text,
                "review": r.select_one(".review-text").text,
                "date": date_text,
                "source": "Capterra"
            })

    return reviews
