
data = 'ini adalah string'
print(data)
print(type(data))

# Cara membuat string

'''
    1. Menggunakan single quote '...'
    2. Menggunakan double quote "..."
'''
data = 'menggunakan single quote'
print(data)

data = "menggunakan double quote"
print(data)

# 2. Menggunakan tanda \

# membuat tanda ' menjadi strng
print('ini adalah hari jum\'at')
print('g\'day, isn\'t it?')

# backlash
print("C:\\user\\ucup")

# Tab
print("ucup\tmarkucup")

# backspace
print("ucup \bmarkucup")

# newline
print("baris pertama,\nbaris kedua")
print("baris pertama,\rbaris kedua.")
print('baris pertama,\r\nbaris kedua')  # dipakai windows

# 3. String Literal atau raw
# hati hati
print('C:\new-folder')

# menggunakan raw string
print(r'C:\new Folder')

# Multiline literal string
print("""
Nama : Ucup
Kelas : 3 SMP
""")

# multiline literal string dan raw
print(r"""
Nama : Faisal
Kelas: 4 SD
Website : www.faisalcokk\newUser
""")
