def build_prompt(decision_type):
    return [
        f"Why are you considering this option ({decision_type})?",
        "What are the top 3 pros (benefits)?",
        "What are the top 3 cons (downsides)?",
        "What risks are involved?",
        "What does it cost in terms of money, time, energy?",
        "How emotionally important is this to you (1–10)?",
        "How rationally useful is it for your long-term goals (1–10)?",
        "Is there a strong moral or ethical reason involved?",
        "What’s your biggest hesitation?",
        "What’s your biggest hope if it works out?"
    ]