# Mini-Project-1
### Nama: Daffa Syahrandy Husain
### NIM : 2409116069

### FLOWCHART
![Mini Project 1 hehe](https://github.com/user-attachments/assets/19d1b902-8737-49dd-afd9-c46704550356)





### Penjelasan Code 
### 1. def berguna untuk mendefinisikan sebuah fungsi
#### def hitung_gaji():

### 2. Penginputan nama, nim, jam kerja dan tarif per jam serta menghitung gaji
#### nama = str(input("Masukkan Nama Anda: "))
#### nim = int(input("Masukkan NIM Anda: "))
#### print("Login Berhasil!")
#### print()
#### print("Halo" , nama , "selamat menghitung gaji")
#### print()
#### jam_kerja = int(input("Masukkan Jam Kerja: "))
#### tarif_kerja = int(input("Masukkan Tarif Kerja: "))
#### gaji = jam_kerja * tarif_kerja
#### print("Gaji anda adalah:", gaji)

### 3. Penambahan bonus dari 10% gaji jika jam kerja lebih dari 160 jam menggunakan if dan else
#### if jam_kerja > 160:
#### bonus = 0.10 * gaji
#### total_gaji = bonus + gaji
#### print("Ini adalah gaji dan bonus anda", bonus)
#### else:
#### print("Anda tidak mendapatkan bonus")

### 4. Melakukan pengulangan hitung gaji dengan menggunakan while True
#### while True:
#### hitung_gaji()
#### ulang = input("Apakah anda ingin menghitung ulang gaji? (Y/T): ")
#### if ulang == "t":
#### break
#### print("Terimakasih")

### Output ketika jam kerja tidak lebih dari 160 jam dan memilih tidak menghitung ulang gaji
![Screenshot 2024-09-30 213228](https://github.com/user-attachments/assets/6e87898e-dfcc-4b5e-988f-5efd7311353d)


### Output ketika jam kerja lebih dari 160 jam dan memilih menghitung ulang gaji
![Screenshot 2024-09-30 213400](https://github.com/user-attachments/assets/cd9b41fa-49c0-4567-ba22-6eb7b9a231a8)

