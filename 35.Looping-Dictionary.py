# Looping Dictionary
teman_teman = {
    'sep': 'Asep Kasep',
    'dok': 'Udok Sorodok',
    'dms': 'Dimas Padimas',
    'dud': 'Dudin Samsudin',
    'sat': 'Satio Borolo'
}

# Looping First Try (Yang muncul adalah key nya)
for teman in teman_teman:
    print(teman)
# hasil
# sep
# dok
# dms
# dud
# sat

# operator untuk mengambil item / iteration
keys = teman_teman.keys()
print(keys)
# hasil ( dict_keys(['sep', 'dok', 'dms', 'dud', 'sat']) )

# ===================================================
for key in teman_teman.keys():
    print(teman_teman.get(key))
# Hasil
# Asep Kasep
# Udok Sorodok
# Dimas Padimas
# Dudin Samsudin
# Satio Borolo

# ===================================================
values = teman_teman.values()
# hasil
# dict_values(['Asep Kasep', 'Udok Sorodok', 'Dimas Padimas', 'Dudin Samsudin', 'Satio Borolo'])

for value in teman_teman.values():
    print(value)

# hasil
# Asep Kasep
# Udok Sorodok
# Dimas Padimas
# Dudin Samsudin
# Satio Borolo

# ===================================================

# # Menggunakan Item
items = teman_teman.items()
print(items)
# hasil
# dict_items([('sep', 'Asep Kasep'), ('dok', 'Udok Sorodok'), ('dms', 'Dimas Padimas'), ('dud', 'Dudin Samsudin'), ('sat', 'Satio Borolo')])

for item in teman_teman.items():
    print(item)
# hasil
# ('sep', 'Asep Kasep')
# ('dok', 'Udok Sorodok')
# ('dms', 'Dimas Padimas')
# ('dud', 'Dudin Samsudin')
# ('sat', 'Satio Borolo')

# ===================================================
for key, value in teman_teman.items():
    print(f"key = {key}, value = {value} ")
# hasil
# key = sep, value = Asep Kasep
# key = dok, value = Udok Sorodok
# key = dms, value = Dimas Padimas
# key = dud, value = Dudin Samsudin
# key = sat, value = Satio Borolo
