# LLM Engineering

A focused learning repository for building practical LLM-powered utilities in Python. The current codebase contains Week 1 exercises for scraping website content and summarizing it with either the OpenAI API or a local Ollama model through the OpenAI-compatible client interface.

## Repository Structure

```text
LLM-Engineering/
|-- README.md
`-- Week1/
    |-- README.md
    |-- day1.py
    |-- day2.py
    `-- scraper.py
```

## Contents

| Path | Description |
| --- | --- |
| [`Week1/day1.py`](Week1/day1.py) | Website summarizer that uses the OpenAI API and an `OPENAI_API_KEY` loaded from a `.env` file. |
| [`Week1/day2.py`](Week1/day2.py) | Website summarizer that connects to a local Ollama server through an OpenAI-compatible endpoint. |
| [`Week1/scraper.py`](Week1/scraper.py) | Reusable scraping helpers for extracting page text and links with `requests` and `BeautifulSoup`. |
| [`Week1/README.md`](Week1/README.md) | Week-specific setup notes, usage examples, and script details. |

## Requirements

- Python 3.10 or newer
- `pip`
- Internet access for fetching websites
- An OpenAI API key for `Week1/day1.py`
- A running Ollama server with `llama3.2` available for `Week1/day2.py`

Install the Python dependencies:

```bash
pip install openai python-dotenv requests beautifulsoup4
```

For the OpenAI example, create a `.env` file in the project root or in `Week1/`:

```env
OPENAI_API_KEY=your_api_key_here
```

For the Ollama example, start Ollama and make sure the model is available:

```bash
ollama pull llama3.2
ollama serve
```

## Quick Start

Run the OpenAI-based summarizer:

```bash
cd Week1
python day1.py
```

Run the local Ollama-based summarizer:

```bash
cd Week1
python day2.py
```

Use the scraping helper from another Python file:

```python
from scraper import fetch_website_contents, fetch_website_links

content = fetch_website_contents("https://anthropic.com")
links = fetch_website_links("https://anthropic.com")
```

## Notes

- The example scripts currently summarize `https://anthropic.com`.
- Scraped website text is truncated to 2,000 characters before summarization.
- The repository does not currently include automated tests or a pinned dependency file.

## Roadmap

- Add a `requirements.txt` or `pyproject.toml` for repeatable installs.
- Move example URLs and model names into configuration.
- Add tests for the scraper helpers.
- Expand the weekly folders with additional LLM engineering exercises.
