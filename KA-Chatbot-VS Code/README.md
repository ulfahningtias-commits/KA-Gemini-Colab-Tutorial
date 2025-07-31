# Gemini Chatbot Python

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/)
[![Google Colab](https://colab.research.google.com/assets/colab-badge.svg)](https://colab.research.google.com/)
[![Gemini API](https://img.shields.io/badge/Gemini%20API-Google-brightgreen)](https://ai.google.dev/gemini-api/docs)

Proyek ini adalah chatbot terminal sederhana menggunakan **Google Gemini API** dan Python. Cocok sebagai template dasar untuk eksperimen dengan AI generatif.

## 🛠️ Fitur
- Input teks langsung di terminal
- Menggunakan model `gemini-2.5-flash`
- Logging interaksi pengguna
- Penanganan error dan prompt yang diblokir

## 🚀 Cara Menjalankan

1. Buat file `.env` dan tambahkan:
   ```
   GOOGLE_API_KEY=YOUR_API_KEY
   ```
2. Install dependensi:
   ```
   pip install -r requirements.txt
   ```
3. Jalankan chatbot:
   ```
   python app.py
   ```

## 📄 File
- `app.py`: Versi lengkap dengan logging dan validasi.
- `chatbot.py`: Versi sederhana minimalis.
- `.env`: Tempat menyimpan API key Anda.

## 🧠 Referensi
- [Gemini API Documentation](https://ai.google.dev/gemini-api/docs)

## 📜 Lisensi
MIT License
