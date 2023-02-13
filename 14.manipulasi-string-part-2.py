# Operator dalam bentuk method

# merubah case menjadi string

# Merubah semua ke uppercase

salam = 'bro!'
print('normal = ' + salam)
salam = salam.upper()
print('upper = ' + salam)

# Merubah semua ke lowercase
campuran = 'Aku PinTer BanGett'
print('normal = ' + campuran)
campuran = campuran.lower()
print('lower = ' + campuran)

# pengecekan dengan isX method

# contoh untuk pengecekan lowercase
salam = 'sist'
apakah_lower = salam.islower()  # hasilnya bool
print(salam + " is lower = " + str(apakah_lower))
apakah_upper = salam.isupper()
print(salam + " is upper = " + str(apakah_upper))

# isalpha() / untuk mengecek semuanya huruf
# isalnum() / untuk mengecek huruf dan angka
# isdecimal() / untuk mengecek semua angka
# isspace() / spasi, tab, newline \n
# istitle() / semua kata dimulai dengan huruf kapital

judul = "It Is Okay Not To Be Orkay"
cek_judul = judul.istitle()  # hasilnya pasti boolean
print(judul + " is title = " + str(cek_judul))


# cek komponen startswitch() endswitch()
cek_start = "Sangjamnim Oppa".startswith('Sangjamnim')
print("start = " + str(cek_start))

cek_end = "Sangjamnim Oppa".endswith('Oppa')
print("start = " + str(cek_end))

# Penggabungan komponen join() split()
pisah = ['aku', 'sayang', 'anjeun']
gabung = ','.join(pisah)
print(pisah)
print(gabung)

gabung = ' '.join(pisah)
print(gabung)

gabung = ' ea '.join(pisah)
print(gabung)

# Split
gabung = 'aku ea sayang ea kamu'
print(gabung.split('ea'))


# Alokasi karakter rjust(), ljust(), center()

# rata kanan
kanan = "kanan".rjust(10)
print("'"+kanan+"'")

# rata kiri
kiri = "kiri".ljust(10)
print("'"+kiri+"'")

# tengah tengah
tengah = "tengah".center(20, "-")
print("'"+tengah+"'")

# kebalikannya / strip()
tengah = tengah.strip("-")  # menghilangkan tanda (-)
print("'"+tengah+"'")
