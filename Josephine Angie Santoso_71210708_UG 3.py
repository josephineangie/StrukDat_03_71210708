from fileinput import close


kalimat = input("Masukkan Kalimat: ")
kata = input("Masukkan Kata: ")

kalimat = kalimat.lower().split()
kata = kata.lower()

total = 0

for i in kalimat:
    if i == kata:
        total += 1
    else:
        close

print("Jumlah kata adalah: ", total)
