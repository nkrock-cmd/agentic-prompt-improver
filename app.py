import streamlit as st
from main import process_claim_prompt

st.title("Agentic Prompt Improver for Construction Claims")

raw_prompt = st.text_area("Enter your raw claim prompt:")
if st.button("Improve Prompt"):
    if raw_prompt.strip():
        result = process_claim_prompt(raw_prompt)
        st.markdown("Improved Prompt:")
        st.success(result)
    else:
        st.warning("Please enter a prompt.")
