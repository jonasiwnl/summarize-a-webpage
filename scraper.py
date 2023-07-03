from urllib.request import urlopen
from bs4 import BeautifulSoup    


def scrape(url: str, target: str) -> list[str]:
    """
    Scrape the given URL for the target data

    :param url: The URL to scrape
    :param target: The target data to scrape
    """
    page = urlopen(url)
    soup = BeautifulSoup(page.read().decode("utf-8"), "html.parser")

    # Find and return all the target data
    return soup.find_all(target)
