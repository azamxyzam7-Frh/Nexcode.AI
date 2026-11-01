import gradio as gr
import ollama

MODEL = "qwen2.5:0.5b"
SYSTEM = "Kamu asisten ramah. Jawab singkat dalam bahasa Indonesia."


def balas(pesan, riwayat):
    # Ambil 10 pesan terakhir saja agar tetap ringan
    konteks = [{"role": "system", "content": SYSTEM}]
    for m in riwayat[-10:]:
        konteks.append({"role": m["role"], "content": m["content"]})
    konteks.append({"role": "user", "content": pesan})

    teks = ""
    for potongan in ollama.chat(
        model=MODEL,
        messages=konteks,
        stream=True,
        options={"num_predict": 300},
    ):
        teks += potongan["message"]["content"]
        yield teks  # jawaban muncul bertahap


gr.ChatInterface(
    balas,
    type="messages",
    title="Chatbot Ringan",
    description="Chatbot offline berbasis model kecil.",
).launch()
