# operasi logika atau boolean

# not, or, and, xor

# Not
print('===== Not =====')
a = False
c = not a
print('data a =', a)
print('=== menggunakan Not ===')
print('data c =', c)

# OR (Jika salah satu True, maka hasil nya True)
print('===== OR =====')
a = False
b = False
c = a or b
print(a, 'OR', b, '=', c)
a = False
b = True
c = a or b
print(a, 'OR', b, ' =', c)
a = True
b = False
c = a or b
print(a, ' OR', b, '=', c)
a = True
b = True
c = a or b
print(a, ' OR', b, ' =', c)


# AND (Jika salah satu False, maka hasil nya False)
#     (jika nilai a:True dan b:True, maka hasilnya True)
print('===== AND =====')
a = False
b = False
c = a and b
print(a, 'AND', b, '=', c)
a = False
b = True
c = a and b
print(a, 'AND', b, ' =', c)
a = True
b = False
c = a and b
print(a, ' AND', b, '=', c)
a = True
b = True
c = a and b
print(a, ' AND', b, ' =', c)


# XOR (jika kedua nilai True atau False, maka nilainya False)
# XOR (jika salah satu bernilai True atau False, maka nilainya True)
print('==== XOR =====')
a = False
b = False
c = a ^ b
print(a, 'XOR', b, '=', c)
a = False
b = True
c = a ^ b
print(a, 'XOR', b, ' =', c)
a = True
b = False
c = a ^ b
print(a, ' XOR', b, '=', c)
a = True
b = True
c = a ^ b
print(a, ' XOR', b, ' =', c)
