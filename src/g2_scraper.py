from selenium import webdriver
from selenium.webdriver.common.by import By
from datetime import datetime
import time

def scrape_g2(company, start_date, end_date):
    start_date = datetime.fromisoformat(start_date)
    end_date = datetime.fromisoformat(end_date)

    url = f"https://www.g2.com/products/{company}/reviews"

    driver = webdriver.Chrome()
    driver.get(url)
    time.sleep(5)

    reviews = []

    while True:
        cards = driver.find_elements(By.CLASS_NAME, "review")

        for card in cards:
            date_text = card.find_element(By.CLASS_NAME, "review-date").text
            review_date = datetime.strptime(date_text, "%B %d, %Y")

            if start_date <= review_date <= end_date:
                reviews.append({
                    "title": card.find_element(By.TAG_NAME, "h3").text,
                    "review": card.find_element(By.CLASS_NAME, "review-body").text,
                    "date": date_text,
                    "source": "G2"
                })

        try:
            next_btn = driver.find_element(By.LINK_TEXT, "Next")
            next_btn.click()
            time.sleep(3)
        except:
            break

    driver.quit()
    return reviews
