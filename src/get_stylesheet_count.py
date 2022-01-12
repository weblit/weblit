from src.get_linked_css import get_linked_css
from src.load_response import load_response

def get_stylesheet_count(url):
    styles_url = get_linked_css(url)
    bundled_styles = []

    for style_url in styles_url:
        res = load_response(style_url)
        # append to bundled and output as files

        bundled_styles.append(res.content.decode())

    return len(bundled_styles)
