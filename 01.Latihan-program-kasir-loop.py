def get_login():
    print("-" * 20)
    print("Halaman Login Kasir")
    username = input('Masukan username Kasir: ')
    password = input('Masukan Password Kasir: ')

    if username == 'admin' and password == 'admin':
        print("login Berhasil___\n")
        main_menu()
    else:
        print("login anda gagal, coba lagi!!")
        get_login()


def counter_kasir():
    counter = input('hitung lagi: (y/n)')
    if counter == 'y':
        kasir()
        # print('yes')
    elif counter == 'n':
        print('ingin hitung lagi?')
        tanya()
    else:
        print('input program salah, coba lagi!')


def kasir():
    # Masukan input dari user
    nama_barang = input('Masukan Pesanan Anda: ')
    harga = int(input('Masukan harga barang: '))
    jumlah_beli = int(input("Masukan jumlah yang anda beli: "))

    # Menghitung jumlah harga
    total = harga * jumlah_beli

    # cetak total harga
    print(f"harga total : {nama_barang}, = {total:,} ")

    # input pembayaran dari user
    bayar = int(input("Masukan pembayaran: "))

    # mengecek kembalian
    kurang = total - bayar
    kembalian = bayar - total

    if bayar > total:
        print(f"jumlah kembalian anda adalah: {kembalian:,} ")
    elif bayar == total:
        print('uang anda pas, terimakasih sudah berbelanja')
    else:
        print(f"maaf uang anda tidak cukup, uang and kurang {kurang:,} ")
        counter_kasir()


# Membuat kalkulator
def kalkulator():
    print('=' * 20)
    print('Program Kalkulator')

    print()
    print('Operator')
    print('=' * 10)
    print('1. Tambah')
    print('2. Kurang')
    print('3. Kali')
    print('4. Bagi')
    print('5. Sisa Bagi/Modulus')

    a = int(input('Masukan bilangan pertama: '))
    b = int(input('Masukan bilangan kedua: '))

    operator = int(input("Masukan Operator: "))

    if operator == 1:
        print(f"hasil dari {a} + {b} = {a+b} ")
    elif operator == 2:
        print("hasil dari {} - {} = {} ".format(a, b, (a - b)))
    elif operator == 3:
        print("hasil dari {} * {} = {} ".format(a, b, (a * b)))
    elif operator == 4:
        print("hasil dari {} / {} = {} ".format(a, b, (a / b)))
    elif operator == 5:
        print("hasil dari {} % {} = {} ".format(a, b, (a % b)))
    else:
        print('Masukan operator yang tersedia!')


def main_menu():
    # Membuat daftar menu pada kasir
    print('=' * 10, "MAIN MENU APLIKASI KASIR", '=' * 10)
    print('Selamat Datang Di Aplikasi Kasir')
    print('=' * 10, 'Masukan input Aplikasi', '=' * 10)
    print('1. Program Kasir')
    print('2. Program Kalkulator')
    print('3. Exit Program')

    # Input pilihan
    pilihan = int(input("Pilih Menu: "))

    # Pilihan Menu
    if pilihan == 1:
        kasir()
    elif pilihan == 2:
        kalkulator()
    else:
        print('Program Exit')
        exit()


def tanya():
    tanya = input("Kembali ke Menu? (y/n)")
    if tanya == 'y':
        main_menu()
    elif tanya == 'n':
        exit()
    else:
        print('input salah')
        print('masukan input dengan benar')


if __name__ == '__main__':
    get_login()
