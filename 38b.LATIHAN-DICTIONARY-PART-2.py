import datetime as dt
import os
import string
import random

# template dict mahasiswa

mahasiswa_template = {
    'nama': 'nama',
    'nim': '00000000',
    'sks_lulus': 0,
    'lahir': dt.datetime(1111, 1, 11)
}

data_mahasiswa = {}
while True:
    os.system('cls')

    print(f"{'SELAMAT DATANG':^20}")
    print(f"{'DATA MAHASISWA':^20} ")
    print('-'*20)

    mahasiswa = dict.fromkeys(mahasiswa_template.keys())
    mahasiswa['nama'] = input('Nama Mahasiswa: ')
    mahasiswa['nim'] = input('NIM Mahasiswa: ')
    mahasiswa['sks_lulus'] = int(input('SKS Lulus: '))
    TAHUN_LAHIR = int(input('Tahun Lahir (YYYY): '))
    BULAN_LAHIR = int(input('Bulan Lahir (1-12): '))
    TANGGAL_LAHIR = int(input('Tanggal Lahir (1-31): '))
    mahasiswa['lahir'] = dt.datetime(TAHUN_LAHIR, BULAN_LAHIR, TANGGAL_LAHIR)

    KEY = ''.join((random.choice(string.ascii_uppercase) for i in range(6)))
    data_mahasiswa.update({KEY: mahasiswa})

    print(f"{'KEY':<6} {'Nama':<15} {'NIM':<9} {'SKS':<7} {'Tanggal Lahir'} ")
    print('='*60)

    for mahasiswa in data_mahasiswa:
        KEY = mahasiswa
        NAMA = data_mahasiswa[KEY]['nama']
        NIM = data_mahasiswa[KEY]['nim']
        SKS = data_mahasiswa[KEY]['sks_lulus']
        LAHIR = data_mahasiswa[KEY]['lahir'].strftime("%x")

        print(f"{KEY:<6} {NAMA:<15} {NIM:<9} {SKS:<7}  {LAHIR} ")

    print('\n')
    is_done = input('Tambah Data Lagi (y/n)?')
    if is_done == 'n':
        break

print('akhir dari program, terima kasih!')
