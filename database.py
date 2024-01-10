import pymysql

config = {
    'user': 'root',
    'password': '',
    'host': 'localhost',
    'database': 'motorist',
}

# Membuat koneksi
connection = pymysql.connect(**config)

# Membuat objek cursor
cursor = connection.cursor()

# Melakukan operasi SQL menggunakan cursor
cursor.execute("SELECT * FROM dataset_penjualan")

# Mengambil hasil query
results = cursor.fetchall()

# Menampilkan hasil query
# for row in results:
#     print(row)

# Menutup kursor dan koneksi
cursor.close()
connection.close()
