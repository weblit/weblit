from src.HtmlParser import HtmlParser

htmlparser = HtmlParser("https://apple.com")

css = htmlparser.get_css_paths()
js = htmlparser.get_js_paths()

print("JS Scripts:", js)
print("CSS Stylesheets:", css)
