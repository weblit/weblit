from helpers.clean_attributes import clean_attributes
from utils.get_linked_css_url import get_linked_css_url
from utils.get_linked_scripts_url import get_linked_scripts_url
from src.find_source_css import find_source_css
from src.find_source_script import find_source_script
from src.relative_path import relative_path

class HtmlParser:
    def __init__(self, url) -> None:
        self.url = url
    
    def find_linked_css_urls(self) -> list:
        return get_linked_css_url(self.url)

    def find_linked_css_count(self) -> int:
        return len(get_linked_css_url(self.url))

    def find_linked_scripts_url(self) -> list:
        return get_linked_scripts_url(self.url)

    def find_linked_scripts_count(self) -> int:
        return len(get_linked_scripts_url(self.url))

    def get_css_paths(self):
        result = []
        css = self.find_linked_css_urls()
        for stylesheet in css:
            source = relative_path(
                clean_attributes(find_source_css(stylesheet)), self.url)

            if source != "":
                result.append(source)

        return result

    def get_js_paths(self):
        result = []
        js = self.find_linked_scripts_url()

        for script in js:
            source = relative_path(
                clean_attributes(find_source_script(script)), self.url)

            if source != "":
                result.append(source)

        return result
