from config.database import Database

class BukuModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "buku"

    def get_all_buku(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_buku(self, judul, pengarang, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (judul, pengarang, tahun_terbit) VALUES (%s, %s, %s)"
            val = (judul, pengarang, tahun_terbit)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False

# === METODE BARU: UPDATE ===
    def update_buku(self, buku_id, judul, pengarang, tahun_terbit):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"UPDATE {self.table_name} SET judul=%s, pengarang=%s, tahun_terbit=%s WHERE buku_id=%s"
            val = (judul, pengarang, tahun_terbit, buku_id)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False

    # === METODE BARU: DELETE ===
    def delete_buku(self, buku_id):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"DELETE FROM {self.table_name} WHERE buku_id=%s"
            val = (buku_id,)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False 