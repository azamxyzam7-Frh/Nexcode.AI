"""Nexcode AI - chatbot sederhana memakai API Claude.

Versi ini hanya memakai pustaka bawaan Python (tanpa pip install).

Cara pakai:
1. Atur API key:  export ANTHROPIC_API_KEY="kunci-kamu"
   (Windows: setx ANTHROPIC_API_KEY "kunci-kamu", lalu buka terminal baru)
2. python chatbot.py
"""

import json
import os
import sys
import urllib.error
import urllib.request

NAMA_BOT = "Nexcode AI"
MODEL = "claude-sonnet-5-5"
URL = "https://api.anthropic.com/v1/messages"

API_KEY = os.environ.get("ANTHROPIC_API_KEY")
if not API_KEY:
    sys.exit("API key belum diatur. Setel ANTHROPIC_API_KEY terlebih dahulu.")

SYSTEM = (
    f"Kamu adalah {NAMA_BOT}, asisten yang ramah. "
    "Jawablah dalam bahasa yang dipakai pengguna."
)


def tanya(history):
    data = json.dumps(
        {
            "model": MODEL,
            "max_tokens": 1000,
            "system": SYSTEM,
            "messages": history,
        }
    ).encode("utf-8")
    req = urllib.request.Request(
        URL,
        data=data,
        headers={
            "content-type": "application/json",
            "x-api-key": API_KEY,
            "anthropic-version": "2023-06-01",
        },
    )
    with urllib.request.urlopen(req, timeout=60) as r:
        hasil = json.loads(r.read().decode("utf-8"))
    return "".join(b.get("text", "") for b in hasil["content"])


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
        balasan = tanya(history)
    except urllib.error.HTTPError as e:
        print(f"Kesalahan {e.code}: {e.read().decode('utf-8', 'ignore')}")
        history.pop()
        continue
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
        history.pop()
        continue

    history.append({"role": "assistant", "content": balasan})
    print(f"{NAMA_BOT}: {balasan}\n")
