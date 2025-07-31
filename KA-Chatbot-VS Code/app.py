import google.generativeai as genai
import os
from dotenv import load_dotenv
import logging # Import modul logging

# --- Konfigurasi Logging (Opsional tapi Direkomendasikan) ---
# Membantu dalam debugging dengan mencatat informasi dan error
logging.basicConfig(
    level=logging.INFO, # Mengatur level log: DEBUG, INFO, WARNING, ERROR, CRITICAL
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler(), # Menampilkan log di konsol
        # logging.FileHandler("chatbot.log") # Opsional: menyimpan log ke file
    ]
)
logging.info("Aplikasi chatbot dimulai.")

# --- Memuat Variabel Lingkungan ---
try:
    load_dotenv()
    logging.info(".env file berhasil dimuat.")
except Exception as e:
    logging.error(f"Gagal memuat file .env: {e}")
    print("Error: Gagal memuat file .env. Pastikan ada dan benar.")
    exit() # Keluar jika .env tidak bisa dimuat

API_KEY = os.getenv("GOOGLE_API_KEY")

# --- Validasi API Key ---
if not API_KEY:
    logging.critical("GOOGLE_API_KEY tidak ditemukan di variabel lingkungan.")
    print("Error: GOOGLE_API_KEY tidak ditemukan.")
    print("Pastikan Anda memiliki file .env di direktori yang sama dengan skrip ini,")
    print("dan di dalamnya ada baris seperti: GOOGLE_API_KEY=AIzaSyB**********************")
    exit()

# --- Konfigurasi Google Generative AI ---
try:
    genai.configure(api_key=API_KEY)
    logging.info("Google Generative AI berhasil dikonfigurasi.")
except Exception as e:
    logging.critical(f"Gagal mengonfigurasi Google Generative AI: {e}")
    print(f"Error: Gagal mengonfigurasi Google Generative AI. Pesan: {e}")
    exit() # Keluar jika konfigurasi gagal

# --- Inisialisasi Model dan Sesi Chat ---
try:
    # Periksa apakah model 'gemini-2.5-flash' tersedia atau gunakan default jika tidak
    # Ini mungkin tidak selalu diperlukan, tetapi bisa membantu jika nama model berubah
    # for m in genai.list_models():
    #     if 'generateContent' in m.supported_generative_methods and m.name == 'models/gemini-2.5-flash':
    #         print(f"Menggunakan model: {m.name}")
    #         model = genai.GenerativeModel(m.name)
    #         break
    # else:
    #     print("Model 'gemini-2.5-flash' tidak ditemukan. Menggunakan 'gemini-pro' sebagai fallback.")
    #     model = genai.GenerativeModel('gemini-pro')

    model = genai.GenerativeModel('gemini-2.5-flash') # Tetap gunakan pilihan Anda

    chat_session = model.start_chat(history=[])
    logging.info("Model Gemini dan sesi chat berhasil diinisialisasi.")
except Exception as e:
    logging.critical(f"Gagal menginisialisasi model atau sesi chat Gemini: {e}")
    print(f"Error: Gagal menginisialisasi model Gemini. Pesan: {e}")
    print("Pastikan nama model benar dan Anda memiliki akses ke Gemini API.")
    exit() # Keluar jika inisialisasi model gagal

# --- Pesan Selamat Datang ---
print("---=== Chatbot Gemini Sederhana ===---")
print("Halo! Aku adalah chatbot sederhana Gemini. Ketik 'keluar' untuk berhenti.")
logging.info("Memulai loop interaksi chat.")

# --- Loop Utama Interaksi Chat ---
while True:
    try:
        user_message = input("Kamu: ")

        if not user_message.strip(): # Menangani input kosong
            print("Chatbot: Masukkan pesan Anda.")
            continue # Lanjut ke iterasi berikutnya tanpa mengirim ke API

        if user_message.lower() == 'keluar':
            print("Chatbot: Sampai jumpa! Terima kasih telah berinteraksi.")
            logging.info("Pengguna mengakhiri sesi.")
            break

        # Mengirim pesan dan mendapatkan respons
        response = chat_session.send_message(user_message)
        logging.info(f"Pesan pengguna: '{user_message}'")
        logging.info(f"Respons Gemini: '{response.text}'")
        print("Chatbot:", response.text)

    except genai.types.BlockedPromptException as e:
        # Menangani jika prompt atau respons diblokir oleh kebijakan keamanan
        logging.warning(f"Prompt atau respons diblokir: {e}")
        print("Chatbot: Maaf, konten tersebut mungkin melanggar kebijakan keamanan.")
        print("         Coba formulasi pertanyaan yang berbeda.")
    except Exception as e:
        # Menangani error umum lainnya (koneksi, API error, dll.)
        logging.error(f"Terjadi kesalahan tak terduga: {e}")
        print(f"Maaf, terjadi kesalahan: {e}")
        print("Coba lagi atau ketik 'keluar'.")

logging.info("Aplikasi chatbot berakhir.")