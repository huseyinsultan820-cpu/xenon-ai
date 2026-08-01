from app.ai import ask_ai
from app.banner import show_banner
from app.loading import loading_screen

show_banner()
loading_screen()

print("╔════════════════════════════════════════════╗")
print("║          Xenon AI Terminal v2.0           ║")
print("╚════════════════════════════════════════════╝")
print("Çıkmak için 'çık' yaz.\n")

while True:
    mesaj = input("🟢 Sen > ")

    if mesaj.lower() in ["çık", "cik", "exit", "quit"]:
        print("\n🔴 Xenon AI: Görüşmek üzere!")
        break

    try:
        print("\n🟡 Xenon düşünüyor...\n")
        cevap = ask_ai(mesaj)
        print(f"🤖 Xenon AI > {cevap}\n")
    except Exception as e:
        print(f"\n❌ Hata: {e}\n")
