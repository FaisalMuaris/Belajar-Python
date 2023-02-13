# operator dictionary

data_dict = {
    'sep': 'Asep Saepuloh',
    'udk': 'Udok sii edann',
    'dms': 'Dimas gantennggss'
}


# panjang dictionary
lendict = len(data_dict)
print(f"panjang dictionary = {lendict} ")

# Mengecek key exist
key = 'sep'
checkey = key in data_dict
print(f"Apakah '{key}' ada di datadict: {checkey} ")

# mengakses value (read) dengan get
print(data_dict['sep'])
print(data_dict.get('sep'))
# cek key dengan message 'tidak ditemukan'
print(data_dict.get('lur', 'Key tidak ditemukan!'))

# Mengupdate data dictionary
data_dict['sep'] = 'Asep Nupalih kaler'
print(data_dict)

# Menambah data dict
data_dict['dud'] = 'Dudin nu ganteng juga'
print(data_dict)

data_dict.update({"sep": 'Asep Saepuloh'})
print(data_dict)
# Kalau key tidak ada, key otomatis di tambah
data_dict.update({'fm': "Faisal Muaris"})
print(data_dict)

# delete data pada dictionary
del data_dict['fm']
print(data_dict)
