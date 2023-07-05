import requests
from typing import Union

from errors import WebScrapaError, ErrorCategory


def summarize_many(data: list[str], key: str) -> Union[list[str], WebScrapaError]:
    """
    Summarize the given text using openai

    :param key: The openai api key
    :param text: The text to summarize
    """
    resp = []

    api_url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"

    headers = {
        "Authorization": f"Bearer {key}"
    }

    try:
        for text in data:
            response = requests.post(api_url, headers=headers, json=text)
            resp.append(response.json()[0]["summary_text"])

    # TODO better error handling
    except Exception as exception:
        return None, WebScrapaError(ErrorCategory.HUGGINGFACEERROR, exception)

    return resp, None
