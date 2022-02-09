import re

def find_source_script(script: str) -> str:
    temp_str = str(re.findall(r'src=.*', script)[0])

    return temp_str[5:len(temp_str) - 11] # removing other attributes and tags
