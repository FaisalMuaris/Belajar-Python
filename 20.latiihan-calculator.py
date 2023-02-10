# Latihan

# calculator sederhana
# membuat operator (+, -, *, /)
print(5*"="+" KALKULATOR SEDERHANA " + 5*'=')

angka1 = float(input("Masukan bilangan Pertama : "))
operator = input("Operator (+, -, *, /) : ")
angka2 = float(input('Masukan Bilangan Kedua : '))
if operator == "+":
    hasil = angka1 + angka2
    print(f'Hasil dari {angka1} {operator} {angka2} adalah : {hasil}')
elif operator == "-":
    hasil = angka1 - angka2
    print(f'Hasil dari {angka1} {operator} {angka2} adalah : {hasil}')
elif operator == "*" or operator == "x":
    hasil = angka1 * angka2
    print(f'Hasil dari {angka1} {operator} {angka2} adalah : {hasil}')
elif operator == "/":
    hasil = angka1 / angka2
    print(f'Hasil dari {angka1} {operator} {angka2} adalah : {hasil}')


else:
    print('Operator Tidak Ditemukan!')

print(40*"=")
print("Terima Kasih Sudah menggunakan Calculator ini!")
