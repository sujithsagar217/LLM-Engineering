from bs4 import BeautifulSoup
import requests

# Standard browser headers
headers = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
    )
}


def fetch_website_contents(url):
    """
    Return the title and textual contents of a website.
    Output is truncated to 2,000 characters.
    """

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    title = (
        soup.title.get_text(strip=True)
        if soup.title
        else "No title found"
    )

    text = ""

    if soup.body:
        unwanted_tags = {"script", "style", "img", "input"}

        for tag in soup.find_all(unwanted_tags):
            tag.decompose()

        text = soup.body.get_text(
            separator="\n",
            strip=True
        )

    return f"{title}\n\n{text}"[:2000]


def fetch_website_links(url):
    """
    Return all non-empty links found on the website.
    """

    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()

    soup = BeautifulSoup(response.content, "html.parser")

    return [
        anchor.get("href")
        for anchor in soup.find_all("a")
        if anchor.get("href")
    ]
