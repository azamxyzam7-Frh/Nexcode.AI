"""Nexcode AI - chatbot sederhana memakai API Claude.

Cara pakai:
1. pip install -r requirements.txt
2. Atur API key:  export ANTHROPIC_API_KEY="kunci-kamu"
   (Windows: setx ANTHROPIC_API_KEY "kunci-kamu", lalu buka terminal baru)
3. python chatbot.py
"""

import os
import sys

from anthropic import Anthropic

NAMA_BOT = "Nexcode AI"
MODEL = "claude-sonnet-5-5"

if not os.environ.get("ANTHROPIC_API_KEY"):
    sys.exit("API key belum diatur. Setel ANTHROPIC_API_KEY terlebih dahulu.")

client = Anthropic()  # membaca ANTHROPIC_API_KEY dari environment
history = []

print(f"{NAMA_BOT} siap! Ketik 'keluar' untuk berhenti.\n")

while True:
    teks = input("Kamu: ").strip()
    if not teks:
        continue
    if teks.lower() in ("exit", "keluar"):
        print("Sampai jumpa!")
        break

    history.append({"role": "user", "content": teks})

    try:
        respons = client.messages.create(
            model=MODEL,
            max_tokens=1000,
            system=(
                f"Kamu adalah {NAMA_BOT}, asisten yang ramah. "
                "Jawablah dalam bahasa yang dipakai pengguna."
            ),
            messages=history,
        )
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        history.pop()  # batalkan pesan terakhir agar bisa dicoba lagi
        continue

    balasan = respons.content[0].text
    history.append({"role": "assistant", "content": balasan})
    print(f"{NAMA_BOT}: {balasan}\n")
