import tkinter.messagebox as messagebox
from models.user_model import UserModel
from views.login_view import LoginView
from controllers.buku_controller import BukuController

class AuthController:
    def __init__(self):
        self.model = UserModel()
        self.buka_login()

    def buka_login(self):
        self.view = LoginView()
        self.view.btn_login.configure(command=self.proses_login)
        self.view.mainloop()

    def proses_login(self):
        username = self.view.entry_username.get()
        password = self.view.entry_password.get()

        if not username or not password:
            messagebox.showwarning("Peringatan", "Username dan Password wajib diisi!")
            return

        user = self.model.autentikasi(username, password)

        if user:
            messagebox.showinfo("Login Berhasil", f"Selamat datang, {user['username']} ({user['role']})!")

            # Tutup jendela Login
            self.view.destroy()
            # Buka jendela Utama Perpustakaan dan sediakan fungsi callback untuk kembali ke login saat logout
            app_utama = BukuController(user_role=user['role'], on_logout=self.buka_login)
            app_utama.run()
        else:
            messagebox.showerror("Login Gagal", "Username atau Password salah!")

    def run(self):
        pass


        