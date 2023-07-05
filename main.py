import sys

from scraper import scrape
from summarizer import summarize_many
from env import validate_env


def main():
    print("Starting...")

    env, err = validate_env()
    if err != None:
        print(err)
        sys.exit(1)

    # Scrape
    data, err = scrape(sys.argv[1], "p")
    if err != None:
        print(err)
        sys.exit(1)

    # Summarize
    summaries, err = summarize_many(data, env.get("HUGGINGFACE_API_KEY"))
    if err != None:
        print(err)
        sys.exit(1)

    # Write to file
    with open("output.txt", "w") as f:
        for summary in summaries:
            f.write(f"{summary}\n")

    print("Finished.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <URL>")
        sys.exit(1)

    main()
