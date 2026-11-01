import tkinter.messagebox as messagebox
from models.anggota_model import AnggotaModel
from views.anggota_view import AnggotaView

class AnggotaController:
    def __init__(self):
        self.model = AnggotaModel()
        self.view = AnggotaView()

        self.selected_anggota_id = None

        self.view.btn_simpan.configure(command=self.simpan_data)
        self.view.btn_update.configure(command=self.perbarui_data)
        self.view.btn_hapus.configure(command=self.hapus_data)

        self.view.tabel.bind("<<TreeviewSelect>>", self.pilih_baris)
        self.muat_data_tabel()

    def muat_data_tabel(self):
        for item in self.view.tabel.get_children():
            self.view.tabel.delete(item)

        data_anggota = self.model.get_all_anggota()

        for anggota in data_anggota:
            # Mengambil data berdasarkan key 'anggota_id' dari database
            id_val = anggota.get('anggota_id')
            self.view.tabel.insert("", "end", values=(id_val, anggota['nama'], anggota['alamat']))

    def pilih_baris(self, event):
        selected_item = self.view.tabel.selection()
        if selected_item:
            item = self.view.tabel.item(selected_item)
            values = item['values']
            
            self.selected_anggota_id = values[0]

            self.view.entry_nama.delete(0, 'end')
            self.view.entry_nama.insert(0, values[1])
            
            self.view.entry_alamat.delete(0, 'end')
            self.view.entry_alamat.insert(0, values[2])

    def simpan_data(self):
        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form anggota harus diisi!")
            return

        berhasil = self.model.create_anggota(nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil disimpan!")
            self.bersihkan_form()
            self.muat_data_tabel()
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat menyimpan data anggota.")

    def perbarui_data(self):
        if not self.selected_anggota_id:
            messagebox.showwarning("Peringatan", "Pilih data anggota yang ingin diperbarui dari tabel!")
            return

        nama = self.view.entry_nama.get()
        alamat = self.view.entry_alamat.get()

        if not nama or not alamat:
            messagebox.showwarning("Peringatan", "Semua kolom form anggota harus diisi!")
            return

        berhasil = self.model.update_anggota(self.selected_anggota_id, nama, alamat)

        if berhasil:
            messagebox.showinfo("Sukses", "Data anggota berhasil diperbarui!")
            self.bersihkan_form()
            self.muat_data_tabel()
            self.selected_anggota_id = None
        else:
            messagebox.showerror("Error", "Terjadi kesalahan saat memperbarui data anggota.")

    def hapus_data(self):
        if not self.selected_anggota_id:
            messagebox.showwarning("Peringatan", "Pilih data anggota yang ingin dihapus dari tabel!")
            return

        konfirmasi = messagebox.askyesno("Konfirmasi", "Apakah Anda yakin ingin menghapus data anggota ini?")
        if konfirmasi:
            berhasil = self.model.delete_anggota(self.selected_anggota_id)

            if berhasil:
                messagebox.showinfo("Sukses", "Data anggota berhasil dihapus!")
                self.bersihkan_form()
                self.muat_data_tabel()
                self.selected_anggota_id = None
            else:
                messagebox.showerror("Error", "Terjadi kesalahan saat menghapus data anggota.")

    def bersihkan_form(self):
        self.view.entry_nama.delete(0, 'end')
        self.view.entry_alamat.delete(0, 'end')

    def run(self):
        self.view.mainloop()