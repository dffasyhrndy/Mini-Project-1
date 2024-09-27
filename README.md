# Mini-Project-1
### Nama: Daffa Syahrandy Husain
### NIM : 2409116069

### FLOWCHART
![Mini Project 1](https://github.com/user-attachments/assets/2c550463-60fa-42f4-aa5c-a1c8f1102952)



### Penjelasan Code 
### def berguna untuk mendefinisikan sebuah fungsi, dan fungsi yang dipakai adalah hitung_gaji()
def hitung_gaji():

### Penginputan jam kerja dan tarif per jam serta menghitung gaji
#### jam_kerja = int(input("Masukkan Jam Kerja: "))
#### tarif_kerja = int(input("Masukkan Tarif Kerja: "))
#### gaji = jam_kerja * tarif_kerja
#### print("Gaji anda adalah:", gaji)

### Penambahan bonus dari 10% gaji jika jam kerja lebih dari 160 jam menggunakan if dan else
#### if jam_kerja > 160:
#### bonus = 0.10 * gaji + gaji
#### print("Ini adalah gaji dan bonus anda", bonus)
#### else:
#### print("Anda tidak mendapatkan bonus")

### Melakukan pengulangan hitung gaji dengan menggunakan while True
#### while True:
#### hitung_gaji()
#### ulang = input("Apakah anda ingin menghitung ulang gaji? (Y/T): ")
#### if ulang == "t":
#### break
#### print("Terimakasih")
