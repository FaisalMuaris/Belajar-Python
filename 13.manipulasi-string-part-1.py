# Manipulasi String

# 1. Menyambungkan string (concatenate)
nama_pertama = 'ucup'
nama_tengah = 'suparta'
nama_akhir = 'pamungkas'

nama_lengkap = nama_pertama + " "+nama_tengah + " " + nama_akhir
print(nama_lengkap)

# 2. Menghitung panjang string
# ====================================
#                 len
# ====================================
panjang = len(nama_lengkap)
print("Panjang dari " + nama_lengkap + " = " + str(panjang))

# 3. Operator untuk string

# mengecek apakah ada komponen char atu string, di string

k = "k"
status = k in nama_lengkap

print(k + " ada di " + nama_lengkap + " = " + str(status))

K = "K"
status = K in nama_lengkap

print(K + " ada di " + nama_lengkap + " = " + str(status))

k = "k"
status = k not in nama_lengkap

print(k + " ada di " + nama_lengkap + " = " + str(status))

# Mengulang String
print('wk'*10)
print(10*'wk')

# =========================================
# Indexing
# =========================================
# Dari depan
print("index ke-0 : " + nama_lengkap[0])
print("index ke-1 : " + nama_lengkap[1])
# dari belakang
print("index ke-(-1) : " + nama_lengkap[-1])
print("index ke-(-2) : " + nama_lengkap[-2])
print("index ke-[0:3] :" + nama_lengkap[0:3])
print("index ke-[3:8] :" + nama_lengkap[3:8])
print("index ke-[0,2,4,6,8,10] :" + nama_lengkap[0:11:2])


# item paling kecil
print("paling kecil : " + min(nama_lengkap))
# item paling besar
print("paling besar : " + max(nama_lengkap))

ascii_code = ord("'")
print("ASCII code untuk spasi adalah " + str(ascii_code))
data = 117
print("char untuk ASCII 117 adalah " + chr(data))

# ====================================
# 4. operator dalam bentuk method
# ====================================
# ============== COUNT ===============

data = 'otong santong'
jumlah = data.count("o")
print("jumlah o pada " + data + " = " + str(jumlah))
