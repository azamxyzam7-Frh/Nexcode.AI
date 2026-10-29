# Nexcode AI

Chatbot sederhana berbasis API Claude.

## Cara menjalankan

1. Install dependensi:
   ```
   pip install -r requirements.txt
   ```
2. Pasang API key (dari console.anthropic.com):
   ```
   export ANTHROPIC_API_KEY="kunci-kamu"
   ```
   Windows: `setx ANTHROPIC_API_KEY "kunci-kamu"` lalu buka ulang terminal.
3. Jalankan:
   ```
   python chatbot.py
   ```

## Di HP

- **Android (Termux):** `pkg install python git`, clone repo ini, lalu ikuti langkah di atas.
- **Android/iPhone (Codespaces):** buka repo di GitHub → Code → Codespaces → Create codespace, lalu ikuti langkah di atas di Terminal.

## Penting

Jangan pernah meng-upload API key ke GitHub.
