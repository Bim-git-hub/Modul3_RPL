from unittest.mock import MagicMock
from models.buku_model import BukuModel

def test_create_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database agar tidak mengotori data asli
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Melakukan eksekusi fungsi
    hasil = model.create_buku("Buku Testing", "Penulis QA", 2026)

    # Memverifikasi apakah fungsi mengembalikan nilai True
    assert hasil is True

    # Memverifikasi apakah cursor.execute benar-benar dipanggil
    mock_cursor.execute.assert_called_once()

    # Memverifikasi apakah perintah commit (simpan) dipanggil
    model.conn.commit.assert_called_once()


    # === FUNGSI PENGUJIAN BARU ===
def test_get_all_buku_berhasil():
    # Menginisialisasi Model
    model = BukuModel()

    # Memanipulasi (Mock) koneksi database dan cursor
    model.conn = MagicMock()
    mock_cursor = MagicMock()
    model.conn.cursor.return_value = mock_cursor

    # Menyiapkan data dummy yang seolah-olah dikembalikan oleh database
    dummy_data = [
        {"buku_id": 1, "judul": "Algoritma", "pengarang": "Budi", "tahun_terbit": 2023},
        {"buku_id": 2, "judul": "Basis Data", "pengarang": "Ani", "tahun_terbit": 2024}
    ]
    mock_cursor.fetchall.return_value = dummy_data

    # Melakukan eksekusi fungsi get_all_buku
    hasil = model.get_all_buku()

    # Memverifikasi apakah hasil yang dikembalikan sesuai dengan dummy data
    assert hasil == dummy_data
    assert len(hasil) == 2

    # Memverifikasi apakah cursor.execute dipanggil untuk melakukan SELECT
    mock_cursor.execute.assert_called_once()

    # Memverifikasi apakah cursor ditutup dengan benar
    mock_cursor.close.assert_called_once()
