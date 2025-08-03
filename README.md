## Agentic Prompt Improver for Construction Claims
This project refines informal construction-related prompts into formal extension of time (EOT) claims using Google's Gemini LLM.Transform raw, unstructured construction claim prompts into structured, legally sound statements using Gemini LLM

## Features
- Rewrites raw claim prompts to professional format
- API integration using Google Gemini
- Includes multiple test cases and modular logic
- Built with Streamlit UI.
- Designed for use in legal-tech, construction, and claims handling domains

## Objective
Convert vague, unstructured prompts into clear, structured, legally relevant prompts using LLMs.

## Tech Stack
- Python
- Google Gemini LLM
- Streamlit

## Project Structure
agentic-prompt-improver/
── env                     # Gemini API key and secrets
── app.py                  # FastAPI app entry point
── gemini_interface.py     # Handles Gemini LLM calls
── main.py                 # Core logic to run from CLI
── modelcheck.py           # Validate GEMINI model
── prompt_rewriter.py      # Main prompt transformation logic
── test_cases.py           # Sample test cases
── requirements.txt        # Python dependencies
── README.md               # Project Information

## Run Locally - Getting Started
Setup
1.	Clone the repo:
git clone https://github.com/yourusername/agentic-prompt-improver.git
cd agentic-prompt-improver
2.	Create a virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
3.	Install dependencies:
pip install -r requirements.txt
4.	Configure environment variables:
Create a .env file with your Gemini API key:
GEMINI_API_KEY=your_gemini_api_key_here

After Setup:
RUN: streamlit run app.py

## Example:
Input- We can't pour concrete because it's raining.
Output like - 
Subject: Delay in Concrete Pouring Due to Inclement Weather

Dear [Recipient],

We wish to inform you that the scheduled concrete pouring for [Project Name] on [Date] could not proceed due to persistent rainfall...

[Full legal letter with clauses, delay notice, compensation request, etc.]

## Test Cases:
RUN: python test_cases.py

## Approach Summary
The system uses Gemini LLM via API to analyze natural language prompts and rewrite them using formal, contract-ready tone and structure. The core logic includes intent extraction, legal formatting, and adding missing contractual clauses where appropriate.

## Logic, Assumptions, and Limitations
The Agentic Prompt Improver is designed to transform raw, unstructured construction claim prompts into clear, legally sound, and contextually rich versions using LLM capabilities. The core logic involves parsing the user’s input through a prompt_rewriter module which standardizes the language and structure, embedding it with formal contractual terms where necessary. The gemini_interface.py module serves as a bridge to interact with Google Gemini LLM via API, sending the rewritten prompt and fetching refined output. Assumptions include the availability of a stable internet connection for API access, that the raw user prompts are related to construction claims, and that the LLM is capable of understanding domain-specific terminology. Limitations include potential inconsistencies in LLM responses due to token limits or vague inputs, dependency on API reliability and quota, and the fact that the model may not always interpret legal or contractual nuances perfectly without proper context. Therefore, while the tool significantly improves prompt clarity, human verification remains essential before using outputs in legal or contractual communication.

## GitHub Repo
Public repo with clean structure:
https://github.com/nkrock-cmd/agentic-prompt-improver
