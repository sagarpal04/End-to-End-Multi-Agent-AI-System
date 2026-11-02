import re
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from src.tools.tools import web_search, scrape_url

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash",
    temperature=1,
    thinking_budget=0,
)


def build_search_agent():
    def run(query: str) -> str:
        return web_search.invoke(query)
    return run


def build_reader_agent():
    def run(search_results: str) -> str:
        url_match = re.search(r"URL:\s*(https?://\S+)", search_results)
        if not url_match:
            return "No URL found in search results."
        url = url_match.group(1)
        return scrape_url.invoke(url)
    return run


writer_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are an expert research writer. Write clean, structured and insightful reports."),
    ("human",
     """Write a detailed research report on the topic below.

Topic: {topic}

Research gathered:
{research}

Structure the report as:
- Introduction
- Key Findings (minimum 3 well-explained points)
- Conclusion
- Sources (list the URLs found in the research)

Be detailed, factual and professional."""),
])

writer_chain = writer_prompt | llm | StrOutputParser()


critic_prompt = ChatPromptTemplate.from_messages([
    ("system",
     "You are a sharp and constructive research critic. Be honest and specific."),
    ("human",
     """Review the research report below and evaluate it strictly.

Report:
{report}

Respond in this format:
Score: X/10
Strengths:
- ...
Areas to improve:
- ...
One-line verdict: ..."""),
])

critic_chain = critic_prompt | llm | StrOutputParser()
