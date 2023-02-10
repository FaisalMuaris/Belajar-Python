# Teknik menduplikasi List

a = ['Asep', "Udok", "Dimas"]
print(f"a = {a} ")

b = a
print(f"b = {b} ")

# Kita akan merubah member dari a

# Merubah Kedua List
a[1] = "Miguel"
b.sort()

print(f"a = {a} ")
print(f"b = {b} ")

# address dari kedua List a dan b
print(f"address a = {hex(id(a))} ")
print(f"address b = {hex(id(b))} ")

# Menduplikat List dengan copy

print("membuat list c dengan a.copy")
c = a.copy()  # FUll duplikat / membuat data baru

print(f"address a = {hex(id(a))} ")
print(f"address b = {hex(id(b))} ")
print(f"address c = {hex(id(c))} ")

print(f"a = {a} ")
print(f"b = {b} ")
print(f"c = {c} ")

print("kita ubah data [0]")
c[0] = "Udok"

print(f"a = {a} ")
print(f"b = {b} ")
print(f"c = {c} ")

print("kita ubah data [1]")
c[1] = "Faisal"

print(f"a = {a} ")
print(f"b = {b} ")
print(f"c = {c} ")
