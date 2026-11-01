import gradio as gr
import ollama

MODEL = "qwen2.5:0.5b"
SYSTEM = "Kamu asisten ramah. Jawab singkat dalam bahasa Indonesia."


def ambil_teks(isi):
    # Gradio versi baru kadang mengirim isi pesan berupa daftar
    if isinstance(isi, list):
        return "".join(
            b.get("text", "") if isinstance(b, dict) else str(b) for b in isi
        )
    return str(isi)


def balas(pesan, riwayat):
    konteks = [{"role": "system", "content": SYSTEM}]
    for m in riwayat[-10:]:
        konteks.append({"role": m["role"], "content": ambil_teks(m["content"])})
    konteks.append({"role": "user", "content": ambil_teks(pesan)})

    teks = ""
    for potongan in ollama.chat(
        model=MODEL,
        messages=konteks,
        stream=True,
        options={"num_predict": 300},
    ):
        teks += potongan["message"]["content"]
        yield teks


gr.ChatInterface(
    balas,
    title="Chatbot Ringan",
    description="Chatbot offline berbasis model kecil.",
).launch()