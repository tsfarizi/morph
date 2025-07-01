# 🔧 Morph – Backend API

**Morph** adalah platform pembelajaran interaktif berbasis web API yang dibangun menggunakan **Django** dan **Django REST Framework**, dilengkapi dengan chatbot AI untuk mendampingi pengguna saat mempelajari berbagai topik pemrograman.

Repositori ini merupakan **backend API resmi** yang digunakan oleh aplikasi mobile [**Morph App**](https://github.com/tsfarizi/morph_app), sebuah aplikasi Flutter interaktif dengan fitur belajar dan chat AI secara offline.

---

## ⚙️ Teknologi dan Dependensi

Proyek ini dibangun dengan fondasi teknologi berikut:

- **Python** – Bahasa pemrograman utama
- **Django** – Framework web untuk pengembangan cepat
- **Django REST framework** – Toolkit untuk membangun Web API
- **SQLite** – Database ringan berbasis file (default untuk pengembangan)

---

## 🧩 Struktur Aplikasi Django

Proyek ini terdiri dari beberapa aplikasi Django modular:

- `morph_auth` – Autentikasi pengguna, manajemen profil, progres belajar, dan log chat AI
- `morph_ai` – Mengatur logika pemrosesan chatbot AI dan respons model bahasa
- `morph_lesson` – Menyimpan, menyajikan, dan mengelola konten pelajaran

---

## 🗃️ Struktur Database

### 🔐 `morph_auth`

- **User**
  - `email`, `username`, `password`, `last_login`, dsb.
- **LessonProgress**
  - Melacak pelajaran, halaman terakhir, dan tanggal progres
- **ChatLog**
  - Riwayat percakapan AI & user: `role`, `content`, `timestamp`

### 📘 `morph_lesson`

- **Lesson**
  - Judul pelajaran
- **Page**
  - Nomor halaman, judul, file markdown, dan URL akses file

---

## 🚀 Cara Menjalankan Proyek

1. **Clone repositori**
   ```bash
   git clone https://github.com/tsfarizi/morph.git
   cd morph
   ```

2. **Buat virtual environment (opsional tapi disarankan)**
   ```bash
   python -m venv venv
   # Windows
   venv\Scripts\activate
   # macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependensi**
   ```bash
   pip install Django djangorestframework
   ```

4. **Migrate database**
   ```bash
   python manage.py migrate
   ```

5. **(Opsional) Buat superuser**
   ```bash
   python manage.py createsuperuser
   ```

6. **Jalankan server pengembangan**
   ```bash
   python manage.py runserver
   ```
   Akses server di `http://127.0.0.1:8000/` dan admin panel di `/admin`.

7. **Inisialisasi Data Pelajaran**
   Jalankan skrip `main.py` untuk memuat konten dari direktori `media/lessons`:
   ```bash
   python main.py
   ```

---

## 📜 Tentang Skrip `main.py`

Skrip ini membaca struktur `media/lessons/`, lalu:

- Membuat entitas `Lesson` berdasarkan subfolder (misal: `python`, `javascript`)
- Menghapus `Page` lama agar tidak duplikat
- Membuat ulang `Page` baru berdasarkan file markdown:
  - Nomor urut halaman
  - Judul
  - URL file

> Jalankan kembali skrip ini setiap kali ada perubahan isi pelajaran.

---

## 🧭 Tautan Proyek Terkait

- 📱 **Frontend App Flutter**: [tsfarizi/morph_app](https://github.com/tsfarizi/morph_app)
- 🧠 **Komponen UI Flutter**: [tsfarizi/morph_ui](https://github.com/tsfarizi/morph_ui)

---

## 📚 Penutup

Proyek ini adalah fondasi dari _Morph ecosystem_, tempat belajar tidak hanya tentang sintaks tapi juga bagaimana membangun pengalaman belajar yang _meaningful_ dan _terintegrasi_ dengan teknologi modern.

> Backend ini dibuat agar Morph App tetap ringan, fleksibel, dan berkembang sesuai kebutuhan pengguna masa depan.
