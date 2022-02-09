"""
A simple function to get raw string data response from a specific url
"""
import requests


def get(url: str) -> str:
    r = requests.get(url)

    r.close()

    return r.content.decode()
