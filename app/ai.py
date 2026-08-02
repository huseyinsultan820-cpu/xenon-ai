from groq import Groq
import os

client = Groq(api_key=os.environ["GROQ_API_KEY"])

def ask_ai(message):
    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": (
                    "Sen Xenon AI'sın. "
                    "Her zaman kullanıcının yazdığı dilde cevap ver. "
                    "İç düşünce sürecini gösterme. "
                    "Kısa, doğru ve net cevaplar ver."
                ),
            },
            {
                "role": "user",
                "content": message,
            },
        ],
    )

    return response.choices[0].message.content
