import requests

def get_raw_html_from_url(url: str) -> str:
    req = requests.get(url)

    req.close()

    return req.content.decode()


def get_raw_html(filename: str) -> str:
    f = open(filename, "r")

    return f.read()
