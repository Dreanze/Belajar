print("Selamat datang di permainan")

playing = input("Apakah anda ingin bermain? ")

if playing.lower() != "oke" :
    quit()

print("Mari Bermain! ")
score = 0

answer = input("Siapa presiden pertama indonesia? ")
if answer.lower() == "soekarno" :
    print("Jawaban Anda Benar! ")
    score += 1
else :
    print("Jawaban Anda Salah! ")

answer = input("Siapa presiden Kedua indonesia? ")
if answer.lower() == "soeharto" :
    print("Jawaban Anda Benar! ")
    score += 1
else :
    print("Jawaban Anda Salah! ")

answer = input("Siapa presiden Ketiga indonesia? ")
if answer.lower() == "habibie" :
    print("Jawaban Anda Benar! ")
    score += 1
else :
    print("Jawaban Anda Salah! ")

print("Selamat kamu menjawab "   + str(score) +   " Jawaban Benar")
print("Selamat kamu menjawab "   + str((score / 3) * 100) +   " %.")