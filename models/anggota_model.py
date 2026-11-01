from config.database import Database

class AnggotaModel:
    def __init__(self):
        self.db = Database()
        self.conn = self.db.get_connection()
        self.table_name = "anggota"

    def get_all_anggota(self):
        if self.conn:
            cursor = self.conn.cursor(dictionary=True)
            query = f"SELECT * FROM {self.table_name}"
            cursor.execute(query)
            result = cursor.fetchall()
            cursor.close()
            return result
        return []

    def create_anggota(self, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()
            query = f"INSERT INTO {self.table_name} (nama, alamat) VALUES (%s, %s)"
            val = (nama, alamat)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False

    def update_anggota(self, anggota_id, nama, alamat):
        if self.conn:
            cursor = self.conn.cursor()
            # Menggunakan kolom anggota_id
            query = f"UPDATE {self.table_name} SET nama=%s, alamat=%s WHERE anggota_id=%s"
            val = (nama, alamat, anggota_id)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False

    def delete_anggota(self, anggota_id):
        if self.conn:
            cursor = self.conn.cursor()
            # Menggunakan kolom anggota_id
            query = f"DELETE FROM {self.table_name} WHERE anggota_id=%s"
            val = (anggota_id,)
            cursor.execute(query, val)
            self.conn.commit()
            cursor.close()
            return True
        return False