judul = " Balok ".center(20, "=")
print(judul)

print('Rumus Luas Balok')
print(' L = 2 x [(p x l) + (p x t) + (l x t)]')

inputPanjang = float(input('masukan panjang balok : '))
inputLebar = float(input('masukan lebar balok : '))
inputTinggi = float(input('masukan tinggi balok : '))

cm = 'cm'
print('nilai yang anda masukan :')
print('Panjang Balok :', inputPanjang, cm)
print('Lebar Balok :', inputLebar, cm)
print('Tinggi Balok :', inputTinggi, cm)

comment = " Hasil ".center(20, "=")
print(comment)

hasil = 2 * ((inputPanjang * inputLebar) +
             (inputPanjang*inputTinggi) + (inputLebar*inputTinggi))
print('Luas Balok Adalah : ', hasil)
