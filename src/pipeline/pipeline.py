from src.agents.agents import (
    build_search_agent,
    build_reader_agent,
    writer_chain,
    critic_chain,
)
from rich.console import Console

console = Console(highlight=False)


def run_research_pipeline(topic: str) -> dict:
    state = {}

    console.print("\n[bold cyan]Step 1: Search agent is working...[/bold cyan]")
    console.print("=" * 50)

    search_agent = build_search_agent()
    state["search_result"] = search_agent(
        f"Find recent, reliable and detailed information about: {topic}"
    )
    console.print(state["search_result"])

    console.print("\n[bold cyan]Step 2: Reader agent is scraping...[/bold cyan]")
    console.print("=" * 50)

    reader_agent = build_reader_agent()
    state["scrape_content"] = reader_agent(state["search_result"])
    console.print(state["scrape_content"])

    console.print("\n[bold cyan]Step 3: Writer is drafting the report...[/bold cyan]")
    console.print("=" * 50)

    research_combined = (
        f"SEARCH RESULTS:\n{state['search_result']}\n\n"
        f"DETAILED SCRAPED CONTENT:\n{state['scrape_content']}"
    )
    state["report"] = writer_chain.invoke({
        "topic": topic,
        "research": research_combined,
    })
    console.print(state["report"])

    console.print("\n[bold cyan]Step 4: Critic is reviewing...[/bold cyan]")
    console.print("=" * 50)

    state["feedback"] = critic_chain.invoke({"report": state["report"]})
    console.print(state["feedback"])

    return state
