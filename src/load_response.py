import requests

def load_response(url):
    res = requests.get(url)

    return res