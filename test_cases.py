from main import process_claim_prompt

test_inputs = [
    "eot due to material delay. how to justify?",
    "subcontractor failed to deliver. what should i write?",
    "client changed the scope. want to ask for extra cost.",
]

for i, test in enumerate(test_inputs):
    print(f"Test Case {i+1}:")
    print("Raw Input:", test)
    print("Improved:", process_claim_prompt(test), end="\n\n")
