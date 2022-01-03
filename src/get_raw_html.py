import requests

def get_raw_html(url):
    r = requests.get(url)

    print(r)

    return r.content