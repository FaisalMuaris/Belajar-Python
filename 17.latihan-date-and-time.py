# Date And Time (Latihan)

import datetime as dt

print('Masukan tanggal, \nbulan dan tahun lahir anda : \n')
tanggal = int(input("Tanggal \t: "))
bulan = int(input("Bulan \t\t: "))
tahun = int(input("Tahun \t\t: "))

# Menampilkan data yang di input
tanggal_lahir = dt.date(tahun, bulan, tanggal)
print(f"Tanggal lahir anda adalah : {tanggal_lahir}")

# Menagmbil data hari ini
hari_ini = dt.date.today()

print(f"hari ini tanggal : {hari_ini}")

umur_hari = hari_ini - tanggal_lahir

# Hanya menggambil data hari menggunakan "days"
umur_tahun = umur_hari.days // 365
# Mengambil sisa bulan dengan modulus
umur_bulan_sisa = (umur_hari.days % 365) // 30

# mengambil data hari dengan ":%A"
print(f"Hari lahir anda adalah : {tanggal_lahir:%A}")

print(f'umur anda adalah: {umur_tahun} Tahun, {umur_bulan_sisa} bulan')
