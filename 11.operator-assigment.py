# Operator yang dapat dilakukan dengan penyingkatan
# operasi ditambah dengan assigment

a = 5  # ini adalah assigment
print('nilai a =', a)

a += 1  # artinya a = a + 1
print('nilai a += 1 =', a)

a -= 2  # artinya adalah a = a - 2
print('nilai a -= 2 =', a)

a *= 5  # artinya adalah a = a * 5
print('nilai a *= 5 =', a)

a /= 2  # artinya adalah a = a / 2
print('nilai a /= 2 =', a)

# Modulus dan Floor devision

b = 10
print('\nnilai b =', b)

b %= 3
print('b % 3 =', b)

b = 10
print('\nnilai b =', b)

b //= 3
print('b //= 3 =', b)

a = 5
print('nilai a =', a)

# Pangkat atau eksponen
a **= 3
print("nilai a **= 3, nilai a menjadi =", a)

# operasi bitwise
# OR
c = True
print('\nnilai c =', c)
c |= False
print("nilai c |= False, nilai c menjadi =", c)
c = False
print('\nnilai c =', c)
c |= False
print("nilai c |= False, nilai c menjadi =", c)
c = False
print('\nnilai c =', c)
c |= False
print("nilai c |= False, nilai c menjadi =", c)

# AND
c = True
print('\nnilai c =', c)
c &= False
print("nilai c &= False, nilai c menjadi =", c)

c = False
print('\nnilai c =', c)

c &= False
print("nilai c &= False, nilai c menjadi =", c)

c = True
print('\nnilai c =', c)

c &= True
print("nilai c &= True, nilai c menjadi =", c)

# XOR
c = True
print('\nnilai c =', c)
c ^= False
print("nilai c ^= False, nilai c menjadi =", c)

c = False
print('\nnilai c =', c)

c ^= False
print("nilai c ^= False, nilai c menjadi =", c)

c = True
print('\nnilai c =', c)

c ^= True
print("nilai c ^= True, nilai c menjadi =", c)


# Geser Geser
d = 0b0100
print('\nnilai d =', format(d, '04b'))
d >>= 2
print("nilai d >>= 2, nilai d menjadi =", format(d, '04b'))
d <<= 1
print("nilai d <<= 1, nilai d menjadi =", format(d, '04b'))
