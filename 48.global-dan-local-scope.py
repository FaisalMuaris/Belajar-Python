# GLOBAL DAN LOCAL SCOPE

nama_global = 'asep'  # variabel global

# akses variabel global dalam fungsi


def fungsi():
    print(f"fungsi menampilkan {nama_global} ")


fungsi()

# akses variabel global dalam loop
for i in range(0, 5):
    print(f"loop ke - {nama_global} ")

# percabangan
if True:
    print(f"if menampilkan {nama_global} ")


# # Variabel Local Scope

def fungsi2():
    nama_local = "asep"  # -> variabel lokal scope


fungsi2()
# print(nama_lokal) # tidak bisa di jalankan

# contoh1 : penggunaan akses variabel


def say_sep():
    print(f"hello, {nama} ")


nama = "asep"
say_sep()

# contoh 2 : merubah variabel program
angka = 0
nama = 'Isal'


def ubah(nilai_baru, nilai_nama):
    global angka  # fungsi ini dapat merubah variabel angka
    global nama
    nama = nilai_nama
    angka = nilai_baru


print(f"Sebelum = {angka}, {nama} ")
ubah(10, "Asep")
print(f"Sesudah = {angka}, {nama} ")

# contoh 3
angka = 0

for i in range(0, 10):
    angka += i
    print(angka)
    angka_dummy = 5

print(angka)
# print(angka_dummy)

if True:
    angka = 7
    angka_dummy = 10

print(angka)
print(angka_dummy)
