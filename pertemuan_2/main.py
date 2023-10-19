import calculate as c


while(True):
     print("Calculator sederhana")
     print("1. Pertambahan")
     print("2. Pengurangan")
     print("3. Perkalian")
     print("4. Pembagian")
     print("5. exit")

     pilih = int(input("Masukan pilihan: "))

     if pilih == 1:
          bil1 = int(input("Masukan angka pertama: "))
          bil2 = int(input("Masukan angka kedua:"))
          result = c.pertambahan(bil1, bil2)
          print("Hasil pertambahan = ",result)
     elif pilih == 2:
          bil1 = int(input("Masukan angka pertama: "))
          bil2 = int(input("Masukan angka kedua:"))
          result = c.pengurangan(bil1, bil2)
          print("Hasil pengurangan = ",result)
     elif pilih == 3:
          bil1 = int(input("Masukan angka pertama: "))
          bil2 = int(input("Masukan angka kedua:"))
          result = c.perkalian(bil1, bil2)
          print("Hasil perkalian = ",result)
     elif pilih == 4:
          bil1 = int(input("Masukan angka pertama: "))
          bil2 = int(input("Masukan angka kedua:"))
          result = c.pembagian(bil1, bil2)
          print("Hasil pembagian = ",result)
     elif pilih == 5:
          print("terimakasih")
          break
     else:
          print("pilihan yang anda masukan tidak ada, coba lagi")