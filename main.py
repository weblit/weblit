from src.get_raw_css import get_raw_css
from src.get_raw_html import get_raw_html
from src.get_stylesheet_count import get_stylesheet_count
from src.load_response import load_response

styles = get_raw_css("https://hashable.space")

print(get_stylesheet_count("https://hashable.space"))