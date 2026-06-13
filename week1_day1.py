"""
Website Summarizer using OpenAI

Features:
1. Fetch website content
2. Send content to an LLM
3. Generate a concise summary
4. Display results in Markdown

Requirements:
pip install openai python-dotenv
"""

import os
from dotenv import load_dotenv
from openai import OpenAI
from scraper import fetch_website_contents


# -----------------------------
# Configuration
# -----------------------------

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

SYSTEM_PROMPT = """
You are a helpful assistant that analyzes website content
and produces a concise summary.

Ignore navigation menus, headers, footers, and other
non-essential content.

Respond in markdown.
"""

USER_PROMPT_PREFIX = """
Here are the contents of a website.

Please provide:
1. A short summary
2. Key points
3. Important news or announcements (if any)

Website Content:
"""


# -----------------------------
# Message Builder
# -----------------------------

def build_messages(website_content: str):
    return [
        {
            "role": "system",
            "content": SYSTEM_PROMPT
        },
        {
            "role": "user",
            "content": USER_PROMPT_PREFIX + website_content
        }
    ]


# -----------------------------
# Website Summarization
# -----------------------------

def summarize_website(url: str) -> str:
    """
    Fetch website content and generate summary.
    """

    website_content = fetch_website_contents(url)

    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=build_messages(website_content)
    )

    return response.choices[0].message.content


# -----------------------------
# Example Usage
# -----------------------------

if __name__ == "__main__":

    url = "https://anthropic.com"

    print(f"\nSummarizing: {url}\n")

    summary = summarize_website(url)

    print(summary)
