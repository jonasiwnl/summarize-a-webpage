from typing import Union

from errors import WebScrapaError, ErrorCategory


def validate_env() -> Union[dict, WebScrapaError]:
    env = {}

    with open(".env", "r") as f:
        for line in f.readlines():
            content = line.split("=")
            if len(content) != 2:
                return None, WebScrapaError(ErrorCategory.MISCERROR, "Invalid .env file")
            
            content[1].strip()

            if content[1].startswith("'") or content[1].startswith('"'):
                content[1] = content[1][1:-1]

            env[content[0]] = content[1]

    if env["HUGGINGFACE_API_KEY"] == None:
        return None, WebScrapaError(ErrorCategory.ENVERROR, "HUGGINGFACE_API_KEY not set")
    
    return env, None
