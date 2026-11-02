import os
import re

import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from langchain_core.tools import tool
from tavily import TavilyClient

load_dotenv()

api_key = os.getenv("TAVILY_API_KEY")

if not api_key:
    raise ValueError("TAVILY_API_KEY is not defined. Add it to your .env file.")

tavily = TavilyClient(api_key=api_key)


@tool
def web_search(query: str) -> str:
    """Search the internet and return the top 5 relevant results."""
    try:
        results = tavily.search(query=query, max_results=5)

        out = []
        for r in results.get("results", []):
            out.append(
                f"Title: {r.get('title', 'N/A')}\n"
                f"URL: {r.get('url', 'N/A')}\n"
                f"Snippet: {(r.get('content') or '')[:300]}"
            )

        return "\n\n----\n\n".join(out) if out else "No results found."

    except Exception as e:
        return f"Search failed: {e}"


@tool
def scrape_url(url: str) -> str:
    """Open a web page URL and extract its main readable text content."""
    try:
        response = requests.get(
            url,
            timeout=10,
            headers={"User-Agent": "Mozilla/5.0"},
        )
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        for tag in soup(["script", "style", "nav", "footer", "header", "aside"]):
            tag.decompose()

        text = soup.get_text(separator=" ")
        text = re.sub(r"\s+", " ", text).strip()
        return text[:3000] or "No readable content found."

    except Exception as e:
        return f"Could not scrape {url}: {e}"