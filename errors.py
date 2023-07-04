from enum import Enum


class ErrorCategory(Enum):
    REQUESTERROR = "request to url"
    SCRAPINGERROR = "website scrape"
    HUGGINGFACEERROR = "huggingface api fetch"
    WRITINGERROR = "write to file"
    ENVERROR = "environment reading"
    MISCERROR = "something, lol"


class WebScrapaError:
    def __init__(self, category: ErrorCategory, message: str):
        self.category = category
        self.message = message


    def __str__(self):
        return f"Error while attempting {self.category}! {self.message}"
