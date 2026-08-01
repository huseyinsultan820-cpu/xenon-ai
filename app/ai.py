from ollama import chat

def ask_ai(message):
    response = chat(
        model="qwen2.5:1.5b",
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen Xenon AI'sın. "
                    "Her zaman kullanıcının yazdığı dilde cevap ver. "
                    "İç düşüncelerini veya muhakeme sürecini gösterme. "
                    "Kısa ve net cevap ver."
                ),
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return response["message"]["content"]
