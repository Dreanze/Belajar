import math

def nilai_absensi(absensi):
    total_absensi = absensi / 18 * 100
    return total_absensi * 0.10

def nilai_uas(uas):
    return uas * 0.40

def nilai_uts(uts):
    return uts * 0.30

def nilai_tugas(tugas):
    return tugas * 0.20


def main():
    while True:
        print("\nSelamat datang di aplikasi pengukuran IPK! ")
        print("penghitungan nilai ipk")

        absensi = float(input("Jumlah absensi : "))
        uas = float(input("Masukan nilai uas : "))
        uts = float(input("Masukan nilai uts  : "))
        tugas = float(input("Masukan nilai tugas : "))

        hasil = nilai_absensi(absensi) + nilai_uas(uas) + nilai_uts(uts) +  nilai_tugas(tugas)
        print(f"hasil penghitungan ipk anda adalah = {hasil:.2f}")

if __name__ == "__main__":
    main()