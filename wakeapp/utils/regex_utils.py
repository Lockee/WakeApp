import re

from pyparsing import Regex

def check_string(text: str, exp: str) -> bool:
    r = re.compile(exp)
    return bool(r.match(text))