print("=================================")
print("        Xenon AI v0.2")
print("=================================")

isim = input("Adın nedir? ")

print(f"\nMerhaba {isim}!")
print("Ben Xenon AI.")
print("Benimle konuşabilirsin.")
print("Çıkmak için 'çık', 'cik', 'exit' veya 'quit' yaz.\n")

while True:
    mesaj = input(f"{isim}: ")

    if mesaj.lower() in ["çık", "cik", "exit", "quit"]:
        print("Xenon AI: Görüşmek üzere!")
        break

    if mesaj.lower() == "merhaba":
        print(f"Xenon AI: Merhaba {isim}! 😊")

    elif mesaj.lower() == "nasılsın":
        print("Xenon AI: İyiyim, teşekkür ederim. Sen nasılsın?")

    elif mesaj.lower() == "adın ne":
        print("Xenon AI: Benim adım Xenon AI.")

    elif mesaj.lower() == "kaç yaşındasın":
        print("Xenon AI: Ben bir yapay zekâyım, yaşım yok.")

    else:
        print(f"Xenon AI: Sen bana '{mesaj}' yazdın.")
        print("Xenon AI: Bu komutu henüz öğrenmedim.")
