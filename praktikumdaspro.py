def hitung_gaji():

    jam_kerja = int(input("Masukkan Jam Kerja: "))
    tarif_kerja = int(input("Masukkan Tarif Kerja: "))
    print()
    gaji = jam_kerja * tarif_kerja
    print("Gaji anda adalah:", gaji)
    print()
    if jam_kerja > 160:
        bonus = 0.10 * gaji + gaji
        print("Ini adalah gaji dan bonus anda", bonus)
    else:
      print("Anda tidak mendapatkan bonus")
print()
while True:
    hitung_gaji()
    print()
    ulang = input("Apakah anda ingin menghitung ulang gaji? (Y/T)")
    if ulang == "t":
        break
print("Terimakasih")
