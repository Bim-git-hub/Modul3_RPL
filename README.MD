# Sistem Informasi Manajemen Perpustakaan (Desktop MVC)

## Deskripsi Singkat Aplikasi
Aplikasi perangkatan lunak desktop berbasis Python dan MySQL yang dirancang dengan pola arsitektur **Model-View-Controller (MVC)**. Dibangun menggunakan pustaka antarmuka grafis modern **CustomTkinter** untuk memudahkan petugas perpustakaan dalam mengelola data buku, anggota, serta transaksi peminjaman secara aman dan terstruktur.

## Struktur Direktori MVC
- `config/` : Berisi konfigurasi koneksi basis data MySQL.
- `models/` : Berisi kelas logika bisnis dan kueri interaksi basis data.
- `views/` : Berisi antarmuka pengguna grafis (*GUI*) desktop.
- `controllers/` : Berisi pengontrol logika yang menghubungkan View dan Model.
- `tests/` : Berisi skrip pengujian otomatis menggunakan `pytest`.
- `.github/workflows/` : Berisi konfigurasi otomatisasi CI Pipeline GitHub Actions[cite: 6].

## Panduan Instalasi & Konfigurasi Database MySQL
1. Pastikan aplikasi **Laragon** terinstal dan jalankan layanan **MySQL**[cite: 6].
2. Buat database baru bernama `perpustakaan` melalui terminal MySQL atau phpMyAdmin[cite: 6].
3. Import atau buat tabel yang diperlukan (`buku`, `anggota`, `peminjaman`, dan `users`) sesuai skema relasional[cite: 6].
4. Klon repositori ini, lalu buat dan aktifkan *virtual environment* Python[cite: 6]:
   ```bash
   python -m venv env
   .\env\Scripts\activate