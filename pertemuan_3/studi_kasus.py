# 1. List

# soal :
# Buatlah sebuah program yang memungkinkan seorang mahasiswa untuk memilih mata kuliah yang ingin diambil dari daftar mata kuliah yang tersedia : 
# 1. Algoritma Pemrograman
# 2. Pengembangan Berorientasi Objek
# 3. Pengembangan Web dan Mobile

# output yg diharapkan program dapat :
# - Program akan menampilkan daftar mata kuliah yang tersedia.
# - Pengguna dapat memasukkan indeks mata kuliah yang ingin diambil (buat agar dapat mengambil ketika indeks ke-1 bukan ke-0).
# - Program mengecek apakah mata kuliah sudah diambil atau belum. 
# - Setelah pengguna selesai memilih mata kuliah, program akan mencetak daftar mata kuliah yang telah dipilih.

# petunjuk :
# - Program dimulai dengan list "matkul" dan list kosong "mata_kuliah_terpilih".
# - Dengan menggunakan "while true" untuk memilih matkul sampai selesai.

# code :
matkul = [
   "1. Algoritma Pemrograman", 
   "2. Pengembangan Berorientasi Objek", 
   "3. Pengembangan Web dan Mobile"
]

mata_kuliah_terpilih = []

print("Mata kuliah yang tersedia :")
for mk in matkul:
   print(mk)

while True:
   indeks = int(input("\nMasukkan indeks mata kuliah yang ingin Anda ambil (-1 untuk selesai) : "))
   if indeks == -1:
       break
   if 1 <= indeks <= len(matkul):
      mata_kuliah_terpilih = mata_kuliah_terpilih + [matkul[indeks - 1]]
      print(f"Anda mengambil mata kuliah {matkul[indeks - 1]}")
   else:
      print("Indeks tidak valid. Indeks harus antara 1 dan", len(matkul))

print("\nMata kuliah yang telah Anda ambil:")
for mk in mata_kuliah_terpilih:
   print(mk)


# 2. Dictionary

# soal :
# Buatlah program untuk mengelola data mahasiswa.

# output yg diharapkan program dapat :
# - Menambahkan data mahasiswa, 
# - Menampilkan data mahasiswa yang telah ditambahkan, 
# - Keluar dari program.

# petunjuk :
# - Program dimulai dengan sebuah dictionary kosong "data_mahasiswa"
# - Memiliki 3 fungsi utama "tambah_mahasiswa()", "tampilkan_mahasiswa()", "keluar()"
# - Memiliki 3 menu "Tambah Data Mahasiswa", "Tampilkan Data Mahasiswa", "Keluar"
# - Menggunakan "while true" agar berjalan terus menerus, sampai memilih menu keluar.

# code :
data_mahasiswa = {}

def tambah_mahasiswa():
	nama = input("Masukkan nama : ")
	npm = input("Masukkan npm : ")
	data_mahasiswa[nama] = {"npm": npm}
	print("Data pengguna ditambahkan.\n")

def tampilkan_mahasiswa():
   if not data_mahasiswa:
      print("Tidak ada data mahasiswa.\n")
   else:
      for nama, info in data_mahasiswa.items():
      	print(f"Nama Pengguna : {nama},\nNPM : {info['npm']}\n")

while True:
   print("Menu:")
   print("1. Tambah Data Mahasiswa")
   print("2. Tampilkan Data Mahasiswa")
   print("3. Keluar")
    
   pilihan = input("\nPilih menu [1/2/3] : ")
    
   if pilihan == "1":
      tambah_mahasiswa()
   elif pilihan == "2":
      tampilkan_mahasiswa()
   elif pilihan == "3":
      print("Berhasil Keluar")
      break 
   else:
      print("Pilihan tidak valid.")