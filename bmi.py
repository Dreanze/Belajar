def hitung_bmi(berat, tinggi):
    return berat / (tinggi ** 2)

def main():
    print("Program Penghitungan BMI")
    berat = float(input("Masukkan berat badan Anda (kg): "))
    tinggi = float(input("Masukkan tinggi badan Anda (m): "))

    bmi = hitung_bmi(berat, tinggi)
    print(f"BMI Anda adalah: {bmi:.2f}")

    if bmi < 18.5:
        print("Status: Kekurangan berat badan")
    elif 18.5 <= bmi < 25:
        print("Status: Normal")
    elif 25 <= bmi < 30:
        print("Status: Kelebihan berat badan")
    else:
        print("Status: Obesitas")

if __name__ == "__main__":
    main()