from typing import Union
import openai

from errors import WebScrapaError, ErrorCategory


def summarize(key: str, data: list[str]) -> Union[list[str], WebScrapaError]:
    """
    Summarize the given text using openai

    :param key: The openai api key
    :param text: The text to summarize
    """
    openai.api_key = key
    resp = []

    try:
        for text in data:
            resp.append(openai.Completion.create(
                model="text-davinci-003",
                prompt="# Python 3 \ndef remove_common_prefix(x, prefix, ws_prefix): \n    x[\"completion\"] = x[\"completion\"].str[len(prefix) :] \n    if ws_prefix: \n        # keep the single whitespace as prefix \n        x[\"completion\"] = \" \" + x[\"completion\"] \nreturn x \n\n# Explanation of what the code does\n\n#",
                temperature=0,
                max_tokens=150,
                top_p=1.0,
                frequency_penalty=0.0,
                presence_penalty=0.0,
            ))
    
    except openai.error.Timeout as texception:
        return None, WebScrapaError(ErrorCategory.OPENAIERROR, texception)

    except openai.error.APIError as apiexception:
        return None, WebScrapaError(ErrorCategory.OPENAIERROR, apiexception)

    except openai.error.APIConnectionError as apiconnexception:
        return None, WebScrapaError(ErrorCategory.OPENAIERROR, apiconnexception)

    except openai.error.InvalidRequestError as invalidreqexception:
        return None, WebScrapaError(ErrorCategory.OPENAIERROR, invalidreqexception)

    except openai.error.AuthenticationError as authexception:
        return None, WebScrapaError(ErrorCategory.OPENAIERROR, authexception)

    except openai.error.PermissionError as permexception:
        return None, WebScrapaError(ErrorCategory.OPENAIERROR, permexception)

    except openai.error.RateLimitError as ratelimitexception:
        return None, WebScrapaError(ErrorCategory.OPENAIERROR, ratelimitexception)

    return resp, None
