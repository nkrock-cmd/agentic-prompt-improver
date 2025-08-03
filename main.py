from prompt_rewriter import rewrite_prompt
from gemini_interface import generate_response

def process_claim_prompt(raw_input: str) -> str:
    structured_prompt = rewrite_prompt(raw_input)
    improved_output = generate_response(structured_prompt)
    return improved_output
