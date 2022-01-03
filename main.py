from src.get_raw_css import get_linked_css
from src.get_raw_html import get_raw_html
from src.load_response import load_response

res = get_linked_css("https://hashable.space")

for r in res:
    _r = load_response(r)

    print(_r.content.decode())