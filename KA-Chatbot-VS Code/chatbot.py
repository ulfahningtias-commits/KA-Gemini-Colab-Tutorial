import google.generativeai as genai
import os
from dotenv import load_dotenv
load_dotenv()
API_KEY = os.getenv("GOOGLE_API_KEY")

if not API_KEY:
    print("Error: GOOGLE_API_KEY tidak ditemukan. Buat file .env dan tambahkan 'GOOGLE_API_KEY=YOUR_API_KEY'.")
    exit()

genai.configure(api_key=API_KEY)

model = genai.GenerativeModel('gemini-2.5-flash')

chat_session = model.start_chat(history=[])

print("Halo! Aku adalah chatbot sederhana Gemini. Ketik 'keluar' untuk berhenti.")

while True:
    user_message = input("Kamu: ")
    if user_message.lower() == 'keluar':
        print("Chatbot: Sampai jumpa!")
        break
    try:
        response = chat_session.send_message(user_message)
        print("Chatbot:", response.text)
    except Exception as e:
        print(f"Maaf, terjadi kesalahan: {e}")
        print("Coba lagi atau ketik 'keluar'.")
