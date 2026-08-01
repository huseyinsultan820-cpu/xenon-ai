from ollama import chat

def ask_ai(message):
    response = chat(
        model="qwen3:4b",
        messages=[
            {
                "role": "user",
                "content": message,
            }
        ],
    )

    return response["message"]["content"]
