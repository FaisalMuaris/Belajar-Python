# elif / else if statement

nama = input('nama kamu siapa? ')

# if kondisi:
#     aksi true
# elif kondisi:
#    aksi True
# elif kondisi:
#     aksi True
# else:
#     aksi false

if nama == "faisal":  # kondisi 1
    print('hai, pinter!')  # aksi true pertama
elif nama == "muaris":  # kondisi 2
    print('hallo, si solehh!')  # aksi true kedua
elif nama == "andini":
    print(f'kamu cantik bangeet sii, {nama}!')
else:
    print('ga kenal bro!')
print('ini adalah akhiir dari program!')
