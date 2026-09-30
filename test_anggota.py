from models.anggota_model import AnggotaModel

model_anggota = AnggotaModel()

# 1. Menguji fungsi Create Anggota
print("Menambahkan data anggota baru...")
model_anggota.create_anggota("Bimo Prakoso Batmomolin", "Palu")
print("Data anggota berhasil disimpan!")

# 2. Menguji fungsi Read Anggota
print("\n=== Daftar Anggota Perpustakaan ===")
daftar_anggota = model_anggota.get_all_anggota()
for anggota in daftar_anggota:
    print(f"[{anggota['id_anggota']}] {anggota['nama']} - {anggota['alamat']}")