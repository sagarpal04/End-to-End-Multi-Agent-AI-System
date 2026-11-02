import streamlit as st
from src.pipeline.pipeline import run_research_pipeline

st.set_page_config(page_title="Researcher Agent", page_icon="🔎", layout="wide")

st.title("🔎 Researcher Agent")
st.caption(
    "Multi-agent AI system: Search -> Read -> Write -> Critique. "
    "Four specialized agents collaborate to produce a research report."
)

topic = st.text_input(
    "Enter a research topic",
    placeholder="e.g. Latest AI agents in 2026",
)

if st.button("Run research pipeline") and topic.strip():
    with st.status("Agents are working...", expanded=True) as status:
        st.write("Search agent, reader agent, writer and critic are running...")
        state = run_research_pipeline(topic)
        status.update(label="Pipeline completed", state="complete")

    with st.expander("Search results"):
        st.write(state["search_result"])

    with st.expander("Scraped content"):
        st.write(state["scrape_content"])

    st.subheader("Final research report")
    st.markdown(state["report"])

    st.download_button(
        "Download report (.md)",
        data=state["report"],
        file_name="research_report.md",
    )

    st.subheader("Critic feedback")
    st.markdown(state["feedback"])

