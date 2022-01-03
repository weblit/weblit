import requests

def get_raw_html(url):
    r = requests.get(url)

    return r.content.decode()