''' *kwargs fungsi (keyword args) '''


def fungsi(nama, tinggi, berat):
    '''fungsi biasa'''
    print(f"{nama} punya tinggi {tinggi} dan berat {berat} ")


fungsi("asep", 183, 80)


def fungsi(**kwargs):
    '''fungsi **kwargs'''
    nama = kwargs['nama']
    tinggi = kwargs['tinggi']
    berat = kwargs['berat']
    print(f"{nama} punya tinggi {tinggi} dan berat {berat} ")


fungsi(nama="asep", tinggi=183, berat=80)


# studi kasus
def math(*args, **kwargs):
    output = 0
    if kwargs['option'] == 'tambah':
        for angka in args:
            output += angka

    elif kwargs['option'] == 'kali':
        output = 1
        for angka in args:
            output *= angka
    else:
        print('Option tidak ada!!')
    return output


tambah = math(1, 4, 3, option="tambah")
print(f"hasil tambah = {tambah} ")
kali = math(1, 4, 3, option="kali")
print(f"hasil kali = {kali} ")

# args mengambil semua argument berupa nilai
# kwargs mengambil data berupa dictionary {'key': 'value'}
