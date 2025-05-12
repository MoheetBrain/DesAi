import requests
from config import GROQ_API_KEY
from prompt_builder import build_prompt

def ask_groq(prompt):
    url = "https://api.groq.com/openai/v1/chat/completions"
    headers = {
        "Authorization": f"Bearer {GROQ_API_KEY}",
        "Content-Type": "application/json"
    }
    data = {
        "model": "llama3-70b-8192",  # ✅ Updated to LLaMA3
        "messages": [
            {"role": "system", "content": "You are DesAi, an AI that helps users make smart decisions by asking thoughtful questions and scoring pros/cons clearly."},
            {"role": "user", "content": prompt}
        ],
        "temperature": 0.7
    }

    response = requests.post(url, headers=headers, json=data)

    try:
        return response.json()["choices"][0]["message"]["content"]
    except KeyError:
        print("❌ Groq API error:\n")
        print("Status:", response.status_code)
        print("Reason:", response.reason)
        print("Response:", response.json())
        return "Sorry, there was a problem processing your request."

if __name__ == "__main__":
    print("🧠 Welcome to DesAi!")

    decision_type = input("What decision do you need help with? ")

    user_answers = {}
    follow_ups = build_prompt(decision_type)

    for question in follow_ups:
        answer = input(question + " ")
        user_answers[question] = answer

    full_prompt = f"The user needs help with: {decision_type}.\nHere are their answers:\n"
    for q, a in user_answers.items():
        full_prompt += f"{q}\nAnswer: {a}\n"

    full_prompt += """

Please evaluate the user's decision and respond with the following:

1. 🎯 A table scoring the 'Do it' and 'Don't do it' options out of 100.
2. ✅ Each score should be broken down into sub-scores with short reasons.
3. 🔚 End with a final recommendation and explanation.
4. Format clearly.
"""

    reply = ask_groq(full_prompt)
    print("\nDesAi says:\n")
    print(reply)