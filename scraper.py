from typing import Tuple
from urllib.request import urlopen, HTTPError, URLError
from bs4 import BeautifulSoup

from errors import WebScrapaError, ErrorCategory


def scrape(url: str, target: str) -> Tuple[list[str], WebScrapaError]:
    """
    Scrape the given URL for the target data

    :param url: The URL to scrape
    :param target: The target data to scrape
    """
    try:
        page = urlopen(url)
        soup = BeautifulSoup(page.read().decode("utf-8"), "html.parser")

    except URLError as uexception:
        return None, WebScrapaError(ErrorCategory.REQUESTERROR, uexception)

    except HTTPError as hexception:
        return None, WebScrapaError(ErrorCategory.SCRAPINGERROR, hexception)

    except AttributeError as aexception:
        return None, WebScrapaError(ErrorCategory.SCRAPINGERROR, aexception)

    except Exception as exception:
        return None, WebScrapaError(ErrorCategory.MISCERROR, exception)

    # Find and return all the target data
    return soup.find_all(target), None
