""" 
Checks for relative path and if present fixes them to a parent url
"""
def relative_path(string: str, parent_url: str) -> str:
    result = string

    if string.startswith("."):
        result = f"{parent_url}/{string[2:]}"
    
    if string.startswith("/"):
        result = f"{parent_url}/{string[1:]}"

    return result
