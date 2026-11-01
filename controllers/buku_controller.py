import tkinter.messagebox as messagebox
from models.buku_model import BukuModel
from views.buku_view import BukuView

class BukuController:
    def __init__(self, user_role="anggota"):
        self.user_role = user_role
        self.model = BukuModel()
        self.view = BukuView()

        # Menampilkan informasi role pada judul jendela aplikasi
        self.view.title(f"Sistem Manajemen Perpustakaan - Mode: {self.user_role.upper()}")

        # Binding tombol simpan
        self.view.btn_simpan.configure(command=self.simpan_data)

        # OTORISASI: Jika bukan admin, nonaktifkan form input dan tombol simpan
        if self.user_role != "admin":
            self.view.btn_simpan.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

            self.view.btn_update.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

            self.view.btn_hapus.configure(state="disabled", text="Akses Terkunci (Khusus Admin)")
            self.view.entry_judul.configure(state="disabled")
            self.view.entry_penulis.configure(state="disabled")
            self.view.entry_tahun.configure(state="disabled")

        self.muat_data_tabel()

        # Binding (mengikat) tombol di View dengan fungsi di Controller
        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)

        # Event ketika baris tabel diklik oleh pengguna
        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)

        # Memuat data ke tabel saat aplikasi pertama kali dibuka
        self.muat_data_tabel()

    def muat_data_tabel(self):
        # Mengosongkan isi tabel di View terlebih dahulu
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        # Mengambil data dari Model (database)
        data_buku = self.model.get_all_buku()

        # Memasukkan data baru ke dalam tabel View
        for buku in data_buku:
            self.view.tabel.insert("", "end", values=(buku['buku_id'], buku['judul'], buku['pengarang'], buku['tahun_terbit']))

    def pilih_baris(self, event):
            # Mengambil baris yang dipilih pada tabel
            selected_item = self.view.tabel.selection()
            if selected_item:
                item = self.view.tabel.item(selected_item)
                values = item['values']
                
                # Menyimpan id_buku
                self.selected_buku_id = values[0]

                # Mengisi form input otomatis dengan data dari baris yang diklik
                self.view.entry_judul.delete(0, 'end')
                self.view.entry_judul.insert(0, values[1])
                
                self.view.entry_penulis.delete(0, 'end')
                self.view.entry_penulis.insert(0, values[2])
                
                self.view.entry_tahun.delete(0, 'end')
                self.view.entry_tahun.insert(0, values[3])

    def simpan_data(self):
        # Proteksi ganda di level Controller
        if self.user_role != "admin":
            messagebox.showerror("Akses Ditolak", "Anda tidak memiliki izin untuk menambah data!")
            return

        judul = self.view.entry_judul.get()
        penulis = self.view.entry_penulis.get()
        tahun = self.view.entry_tahun.get()

        if not judul or not penulis or not tahun:
            messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
            return

        if self.model.create_buku(judul, penulis, tahun):
            messagebox.showinfo("Sukses", "Data buku berhasil disimpan!")
            self.view.entry_judul.delete(0, 'end')
            self.view.entry_penulis.delete(0, 'end')
            self.view.entry_tahun.delete(0, 'end')
            self.view.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Gagal menyimpan data.")

    def run(self):
        self.view.mainloop()

    def perbarui_data(self):
            if not self.selected_buku_id:
                messagebox.showwarning("Peringatan", "Pilih data buku yang ingin diperbarui dari tabel!")
                return

            judul = self.view.entry_judul.get()
            penulis = self.view.entry_penulis.get()
            tahun = self.view.entry_tahun.get()

            if not judul or not penulis or not tahun:
                messagebox.showwarning("Peringatan", "Semua kolom form harus diisi!")
                return

            berhasil = self.model.update_buku(self.selected_buku_id, judul, penulis, tahun)

            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil diperbarui!")
                self.bersihkan_form()
                self.muat_data_tabel()
                self.selected_buku_id = None
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data.")

    def hapus_data(self):
        if not self.selected_buku_id:
            messagebox.showwarning("Peringatan", "Pilih data buku yang ingin dihapus dari tabel!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data buku ini?")
        if konfirmasi:
            berhasil = self.model.delete_buku(self.selected_buku_id)

            if berhasil:
                messagebox.showinfo("Sukses", "Data buku berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
                self.selected_buku_id = None
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data.")

    def bersihkan_form(self):
        self.view.entry_judul.delete(0, 'end')
        self.view.entry_penulis.delete(0, 'end')
        self.view.entry_tahun.delete(0, 'end')

    # Fungsi untuk menyalakan aplikasi
    def run(self):
        self.view.mainloop()

