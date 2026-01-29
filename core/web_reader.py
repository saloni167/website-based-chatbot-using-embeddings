import requests
from bs4 import BeautifulSoup

def read_website(url: str) -> dict:
    try:
        page = requests.get(url, timeout=8)
        page.raise_for_status()
    except Exception:
        return {}

    soup = BeautifulSoup(page.text, "html.parser")

    unwanted = ["nav", "footer", "header", "script", "style", "aside"]
    for tag in unwanted:
        for element in soup.find_all(tag):
            element.decompose()

    content = " ".join(soup.stripped_strings)

    return {
        "content": content,
        "title": soup.title.string if soup.title else "Unknown Page",
        "source": url
    }
