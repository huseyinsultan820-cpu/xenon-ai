from app.ai import ask_ai

print("=" * 40)
print("        Xenon AI v1.0")
print("=" * 40)

print("Gerçek yapay zekâ hazır.")
print("Çıkmak için 'çık' yaz.\n")

while True:
    mesaj = input("Sen: ")

    if mesaj.lower() in ["çık", "cik", "exit", "quit"]:
        print("Xenon AI: Görüşmek üzere!")
        break

    try:
        cevap = ask_ai(mesaj)
        print(f"\nXenon AI: {cevap}\n")
    except Exception as e:
        print(f"\nHata oluştu: {e}\n")
