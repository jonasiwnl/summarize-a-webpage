import sys

import scraper
import summarizer


def main():
    # Scrape
    data = scraper.scrape("https://www.bbc.com/news/world-us-canada-56756556", "p")

    # Summarize
    summaries = summarizer.summarize(sys.argv[1], data)

    # Write to file
    with open("output.txt", "w") as f:
        for summary in summaries:
            f.write(summary)


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <OPEN_AI_KEY>")
        sys.exit(1)

    main()
