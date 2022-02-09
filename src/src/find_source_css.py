import re


def find_source_css(css: str) -> str:
    temp_str = str(re.findall(r'href=.*', css)[0])

    return temp_str[6:len(temp_str) - 4]
