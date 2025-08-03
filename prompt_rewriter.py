def rewrite_prompt(raw_prompt: str) -> str:
    return (
        f"Please rewrite this construction claim in a legally sound, structured way:\n"
        f"'{raw_prompt}'\n"
        f"Ensure the output includes:\n"
        f"- Legal terminology\n"
        f"- Contractual references if applicable\n"
        f"- Time impact and entitlement explanation\n"
        f"- Clarity and formality"
    )

