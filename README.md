# Mini-Project-1
### Nama: Daffa Syahrandy Husain
### NIM : 2409116069

### FLOWCHART
![Mini Project 1 (1)](https://github.com/user-attachments/assets/d428e5a5-9189-4f01-b775-6180e62bf3d2)




### Penjelasan Code 
### 1. def berguna untuk mendefinisikan sebuah fungsi, dan fungsi yang dipakai adalah hitung_gaji()
def hitung_gaji():

### 2. Penginputan jam kerja dan tarif per jam serta menghitung gaji
#### jam_kerja = int(input("Masukkan Jam Kerja: "))
#### tarif_kerja = int(input("Masukkan Tarif Kerja: "))
#### gaji = jam_kerja * tarif_kerja
#### print("Gaji anda adalah:", gaji)

### 3. Penambahan bonus dari 10% gaji jika jam kerja lebih dari 160 jam menggunakan if dan else
#### if jam_kerja > 160:
#### bonus = 0.10 * gaji + gaji
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
![Screenshot 2024-09-27 192715](https://github.com/user-attachments/assets/5f56ebce-9bd6-478b-a7a2-e211e3c3cf8d)

### Output ketika jam kerja lebih dari 160 jam dan memilih menghitung ulang gaji
![Screenshot 2024-09-27 192731](https://github.com/user-attachments/assets/03b9a5da-c988-4f27-8656-e6c8cc5f6817)
