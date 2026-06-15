# Week 1: Website Scraping and Summarization

Week 1 introduces a simple end-to-end LLM workflow:

1. Fetch a public website.(try different methods)
2. Remove non-content HTML such as scripts, styles, images, and inputs.
3. Extract readable text.
4. Send the extracted content to an LLM.
5. Return a Markdown summary with an overview, key points, and important announcements.

## Files

| File | Purpose |
| --- | --- |
| [`scraper.py`](scraper.py) | Shared website scraping utilities. Includes `fetch_website_contents()` for text extraction and `fetch_website_links()` for collecting links. |
| [`day1.py`](day1.py) | OpenAI API summarization example using `gpt-4.1-mini` and an API key loaded from `.env`. |
| [`day2.py`](day2.py) | Local LLM summarization example using Ollama at `http://localhost:11434/v1` with the `llama3.2` model. |

## Setup

Install dependencies from the repository root or this folder:

```bash
pip install openai python-dotenv requests beautifulsoup4
```

### OpenAI Example

Create a `.env` file with your API key:

```env
OPENAI_API_KEY=your_api_key_here
```

Then run:

```bash
python day1.py
```

### Ollama Example

Install Ollama, pull the model, and start the local server:

```bash
ollama pull llama3.2
ollama serve
```

Then run:

```bash
python day2.py
```

## Script Details

### `scraper.py`

Provides two helper functions:

- `fetch_website_contents(url)`: fetches a page, extracts the title and body text, removes noisy tags, and returns the first 2,000 characters.
- `fetch_website_links(url)`: fetches a page and returns all non-empty anchor `href` values.

### `day1.py`

Uses:

- `python-dotenv` to load `OPENAI_API_KEY`
- `OpenAI` from the official OpenAI Python SDK
- `fetch_website_contents()` from `scraper.py`
- `gpt-4.1-mini` for summarization

### `day2.py`

Uses:

- The OpenAI Python SDK pointed at Ollama's local OpenAI-compatible API
- `requests` and `BeautifulSoup` for scraping
- `llama3.2` for local summarization

## Current Defaults

- Example URL: `https://anthropic.com`
- Request timeout: 10 seconds
- Scraped content limit: 2,000 characters
- Output format: Markdown

## Troubleshooting

| Issue | Check |
| --- | --- |
| `ModuleNotFoundError` | Re-run the dependency installation command. |
| Missing OpenAI credentials | Confirm `.env` contains `OPENAI_API_KEY` and run `day1.py` from a directory where the file can be loaded. |
| Ollama connection error | Confirm `ollama serve` is running and reachable at `http://localhost:11434`. |
| Website fetch failure | Confirm the URL is reachable and the website allows normal HTTP requests. |
