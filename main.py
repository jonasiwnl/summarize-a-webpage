import sys

import scraper
import summarizer


def main():
    print("Starting...")

    # Scrape
    data, err = scraper.scrape("https://www.bbc.com/news/world-us-canada-56756556", "p")
    if err != None:
        print(err)
        sys.exit(1)

    # Summarize
    summaries, err = summarizer.summarize_many(sys.argv[1], data)
    if err != None:
        print(err)
        sys.exit(1)

    # Write to file
    with open("output.txt", "w") as f:
        for summary in summaries:
            f.write(summary)

    print("Finished.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <OPEN_AI_KEY>")
        sys.exit(1)

    main()
