from models.buku_model import BukuModel

model = BukuModel()

# 1. Menguji fungsi Create (menambah buku baru)
# print("Menambahkan data buku...")
# model.create_buku("Pemrograman Python Repository", "Guido van Rossum", 2024)
# print("Data berhasil disimpan ke Laragon MySQL!")


# 3. Menguji fungsi Update (Mengubah data)
print("Mengubah data buku...")
model.update_buku(15, "Pemrograman Python MVC V2", "Pidi Baiq", 2024)
print("Data berhasil diubah!")

# 4. Menguji fungsi Delete (Menghapus data)
# Silakan hapus tanda pagar (#) pada 2 baris di bawah ini jika ingin menguji fungsi hapus. 
print("\nMenghapus data buku...")
model.delete_buku(16) 

# 2. Menguji fungsi Read (menampilkan data)
print("\n=== Daftar Buku ===")
daftar_buku = model.get_all_buku()
for buku in daftar_buku:
    print(f"[{buku['id_buku']}] {buku['judul']} - {buku['penulis']} ({buku['tahun_terbit']})")
