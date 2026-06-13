from openai import OpenAI
import requests
from bs4 import BeautifulSoup


# --------------------------------------------------
# Connect to Local Ollama
# --------------------------------------------------

client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama"
)


# --------------------------------------------------
# Browser Headers
# --------------------------------------------------

HEADERS = {
    "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/117.0.0.0 Safari/537.36"
}


# --------------------------------------------------
# Website Scraper
# --------------------------------------------------

def fetch_website_contents(url):

    response = requests.get(
        url,
        headers=HEADERS,
        timeout=10
    )

    response.raise_for_status()

    soup = BeautifulSoup(
        response.content,
        "html.parser"
    )

    title = (
        soup.title.get_text(strip=True)
        if soup.title
        else "No title found"
    )

    text = ""

    if soup.body:

        for tag in soup.find_all(
            ["script", "style", "img", "input"]
        ):
            tag.decompose()

        text = soup.body.get_text(
            separator="\n",
            strip=True
        )

    return f"{title}\n\n{text}"[:2000]


# --------------------------------------------------
# Prompts
# --------------------------------------------------

SYSTEM_PROMPT = """
You are an expert website analyst.

Summarize the website content and provide:

1. Overview
2. Key Points
3. Important News/Announcements

Ignore navigation menus and footer content.

Respond in markdown.
"""


def build_messages(content):

    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": content
        }
    ]


# --------------------------------------------------
# Llama 3.2 Summary
# --------------------------------------------------

def summarize_website(url):

    website_content = fetch_website_contents(url)

    response = client.chat.completions.create(
        model="llama3.2",
        messages=build_messages(
            website_content
        )
    )

    return response.choices[0].message.content


# --------------------------------------------------
# Example
# --------------------------------------------------

if __name__ == "__main__":

    url = "https://anthropic.com"

    summary = summarize_website(url)

    print(summary)
