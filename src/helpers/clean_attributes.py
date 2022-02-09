"""
Cleans html tags and any attributes other than the attribute specificed and return it's value.

For example:
if `https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-1BmE4kWBq78iYhFldvKuhfTAU6auU8tT94WrHftjDbrCEXSU1oBoqyl2QvZ6jIW3" crossorigin="anonymo` is the input, the output is `https://cdn.jsdelivr.net/npm/bootstrap@5.1.3/dist/css/bootstrap.min.css`
"""
import re


def clean_attributes(input: str):
    try:
        return re.findall(r'(.*\.css|.*\.jsx|.*\.js)', input)[0]
    except IndexError:
        return ""
