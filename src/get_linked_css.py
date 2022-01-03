import re as regex
from src.get_raw_html import get_raw_html

"""
Gets all linked css associated to the specific url
"""
def get_linked_css(url):
    final_matches = []

    res = str(get_raw_html(url))

    matches = regex.findall('link .*', res)

    for _match in matches:
        match = str(_match)

        if match.find("href=") != -1:
            start_index = match.index("href='")
            end_index = -2

            final_matches.append(match[start_index+6:end_index-1])

    
    return final_matches