import datetime

mahasiswa1 = {
    'nama': 'Asep Sikasep',
    'nim': '30012023',
    'sks_lulus': 130,
    'beasiswa': False,
    'lahir': datetime.datetime(1999, 5, 10)
}

mahasiswa2 = {
    'nama': 'Dimas Majid',
    'nim': '30012024',
    'sks_lulus': 140,
    'beasiswa': True,
    'lahir': datetime.datetime(2002, 7, 10)
}

mahasiswa3 = {
    'nama': 'Udok Nyolodok',
    'nim': '30012025',
    'sks_lulus': 110,
    'beasiswa': True,
    'lahir': datetime.datetime(2000, 10, 10)
}

data_mhs = {
    'MAH001': mahasiswa1,
    'MAH002': mahasiswa2,
    'MAH003': mahasiswa3,
}

print(f"{'KEY':<6} {'Nama':<15} {'NIM':<9} {'SKS':<7} {'Beasiswa':<10} {'Lahir'} ")
print('='*60)

for mahasiswa in data_mhs:
    KEY = mahasiswa
    NAMA = data_mhs[KEY]['nama']
    NIM = data_mhs[KEY]['nim']
    SKS = data_mhs[KEY]['sks_lulus']
    BEASISWA = data_mhs[KEY]['beasiswa']
    LAHIR = data_mhs[KEY]['lahir'].strftime("%x")

    print(f"{KEY:<6} {NAMA:<15} {NIM:<9} {SKS:<7} {BEASISWA:^10} {LAHIR} ")
