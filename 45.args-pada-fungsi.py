''' *args '''

# memasukan data/argument


def fungsi(nama, tinggi, berat):
    print(f"{nama} punya tinggi {tinggi} dan berat {berat} ")


fungsi("Asep", 170, 50)


def fungsi(data_list):
    data = data_list.copy()
    nama = data[0]
    tinggi = data[1]
    berat = data[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat} ")


fungsi(["Udin", 100, 120])


# Kenalan dengan args

def fungsi(*args):
    nama = args[0]
    tinggi = args[1]
    berat = args[2]
    print(f"{nama} punya tinggi {tinggi} dan berat {berat} ")


fungsi("Usep", 160, 100)


# studi kasus

def tambah(*data):
    # data adalah tipe nya tuple, dia bisa di iterasi
    output = 0
    for angka in data:
        output += angka

    return output


hasil = tambah(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(f"hasil = {hasil} ")

hasil = tambah(5, 10, 3, 5, 6, 62, 3)
print(f"hasil = {hasil} ")
