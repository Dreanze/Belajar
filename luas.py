import math

def luas_persegi():
    sisi = float(input("Masukkan panjang sisi: "))
    return sisi * sisi

def luas_persegi_panjang():
    panjang = float(input("Masukkan panjang: "))
    lebar = float(input("Masukkan lebar: "))
    return panjang * lebar

def luas_segitiga():
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    return 0.5 * alas * tinggi

def luas_lingkaran():
    jari_jari = float(input("Masukkan jari-jari: "))
    return math.pi * jari_jari ** 2

def luas_jajar_genjang():
    alas = float(input("Masukkan alas: "))
    tinggi = float(input("Masukkan tinggi: "))
    return alas * tinggi

def luas_trapesium():
    sisi_atas = float(input("Masukkan panjang sisi atas: "))
    sisi_bawah = float(input("Masukkan panjang sisi bawah: "))
    tinggi = float(input("Masukkan tinggi: "))
    return 0.5 * (sisi_atas + sisi_bawah) * tinggi

def luas_belah_ketupat():
    d1 = float(input("Masukkan diagonal 1: "))
    d2 = float(input("Masukkan diagonal 2: "))
    return 0.5 * d1 * d2

def luas_layang_layang():
    d1 = float(input("Masukkan diagonal 1: "))
    d2 = float(input("Masukkan diagonal 2: "))
    return 0.5 * d1 * d2

def main():
    while True:
        print("\nKalkulator Luas Bangun Datar")
        print("1. Persegi")
        print("2. Persegi Panjang")
        print("3. Segitiga")
        print("4. Lingkaran")
        print("5. Jajar Genjang")
        print("6. Trapesium")
        print("7. Belah Ketupat")
        print("8. Layang-Layang")
        print("9. Keluar")
        
        pilihan = input("Pilih bangun datar (1-9): ")
        
        if pilihan == '1':
            hasil = luas_persegi()
            print(f"Luas persegi: {hasil}")
        elif pilihan == '2':
            hasil = luas_persegi_panjang()
            print(f"Luas persegi panjang: {hasil}")
        elif pilihan == '3':
            hasil = luas_segitiga()
            print(f"Luas segitiga: {hasil}")
        elif pilihan == '4':
            hasil = luas_lingkaran()
            print(f"Luas lingkaran: {hasil:.2f}")
        elif pilihan == '5':
            hasil = luas_jajar_genjang()
            print(f"Luas jajar genjang: {hasil}")
        elif pilihan == '6':
            hasil = luas_trapesium()
            print(f"Luas trapesium: {hasil}")
        elif pilihan == '7':
            hasil = luas_belah_ketupat()
            print(f"Luas belah ketupat: {hasil}")
        elif pilihan == '8':
            hasil = luas_layang_layang()
            print(f"Luas layang-layang: {hasil}")
        elif pilihan == '9':
            print("Terima kasih telah menggunakan program ini!")
            break
        else:
            print("Pilihan tidak valid. Silakan pilih 1-9.")

if __name__ == "__main__":
    main()