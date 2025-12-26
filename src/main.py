import argparse
from g2_scraper import scrape_g2
from capterra_scraper import scrape_capterra
from trustpilot_scraper import scrape_trustpilot
import json

parser = argparse.ArgumentParser()
parser.add_argument("--company", required=True)
parser.add_argument("--source", required=True)
parser.add_argument("--start", required=True)
parser.add_argument("--end", required=True)

args = parser.parse_args()

if args.source.lower() == "g2":
    reviews = scrape_g2(args.company, args.start, args.end)
elif args.source.lower() == "capterra":
    reviews = scrape_capterra(args.company, args.start, args.end)
elif args.source.lower() == "trustpilot":
    reviews = scrape_trustpilot(args.company, args.start, args.end)
else:
    raise ValueError("Invalid source")

with open("output/reviews.json", "w", encoding="utf-8") as f:
    json.dump(reviews, f, indent=4)

print("✅ Reviews saved successfully")
