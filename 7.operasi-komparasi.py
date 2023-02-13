# Operator Komparasi

# setiap hasil dari operasi komparasi adalah boolean

# >, <, >=, <=, ==, !=, is, is not

a = 4
b = 2

#  lebih besar dari >
print("========Lebih besar dari (>)")
hasil = a > 3
print(a, ">", 3, "=", hasil)
hasil = b > 3
print(a, ">", 3, "=", hasil)
hasil = b > 2
print(a, ">", 3, "=", hasil)

#  kurang dari <

print("======== kurang dari (<)")
hasil = a < 3
print(a, "<", 3, "=", hasil)
hasil = b < 3
print(a, "<", 3, "=", hasil)
hasil = b < 2
print(a, "<", 3, "=", hasil)

#  lebih besar dari sama dengan >=
print("========Lebih besar dari sama dengan (>=)")
hasil = a >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 3
print(a, ">=", 3, "=", hasil)
hasil = b >= 2
print(a, ">=", 3, "=", hasil)

#  kurang dari sama dengan <=

print("======== kurang dari (<)")
hasil = a <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 3
print(a, "<=", 3, "=", hasil)
hasil = b <= 2
print(a, "<=", 3, "=", hasil)

# Sama dengan ==
print("======== sama dengan (==)")
hasil = a == 4
print(a, '==', 4, '=', hasil)
hasil = b == 4
print(b, '==', 4, '=', hasil)

# tidak Sama dengan ==
print("======== tidak sama dengan (!=)")
hasil = a != 4
print(a, '!=', 4, '=', hasil)
hasil = b != 4
print(b, '!=', 4, '=', hasil)


# 'is' sebagai komparasi object identity
print("======== object identity (is)")
x = 5  # ini adalah assigment membuat object
y = 6
print('nilai x adalah,', x, '. id = ', hex(id(x)))
print('nilai y adalah,', y, '. id = ', hex(id(y)))
hasil = x is y
print('x is y =', hasil)

# 'is not' sebagai komparasi object identity
print("======== object identity (is not)")
x = 5  # ini adalah assigment membuat object
y = 6
print('nilai x adalah,', x, '. id = ', hex(id(x)))
print('nilai y adalah,', y, '. id = ', hex(id(y)))
hasil = x is not y
print('x is y =', hasil)
