# WIdth and Multiline

# Data

data_nama = "ujang surjang"
data_umur = 18
data_tinggi = 173.1
data_nomor_sepatu = 43

# string standar
data_string = f"nama = {data_nama}, umur = {data_umur}, tinggi = {data_tinggi}, nomor sepatu = {data_nomor_sepatu}"
print(5*"=" + " Data String " + 5*"=")
print(data_string)


# String multiline (menggunakan enter, newline,\n)
data_string = f"nama = {data_nama}, \numur = {data_umur}, \ntinggi = {data_tinggi}, \nnomor sepatu = {data_nomor_sepatu}"
print("\n"+5*"=" + " Data String " + 5*"=")
print(data_string)

# String multiline menggunakan """"---""""

data_string = f"""nama = {data_nama}
umur = {data_umur}
tinggi = {data_tinggi}
sepatu = {data_nomor_sepatu}
"""
print("\n"+5*"=" + " Data String " + 5*"=")
print(data_string)

# Mengatur lebarnya
data_nama = "Ujang"
data_string = f"""
nama    = {data_nama:>5}
umur    = {data_umur:>5}
tinggi  = {data_tinggi:>5}
sepatu  = {data_nomor_sepatu:>5}
"""
print("\n"+5*"=" + " Data String " + 5*"=")
print(data_string)
