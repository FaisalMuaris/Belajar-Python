# copy dictionary
teman_teman = {
    'sep': 'Asep Kasep',
    'dok': 'Udok Sorodok',
    'dms': 'Dimas Padimas',
    'dud': 'Dudin Samsudin',
    'sat': 'Satio Borolo'
}

friends = teman_teman.copy()

print(f"teman-teman = {teman_teman} \n")
print(f"Friends = {friends} \n")

teman_teman['dms'] = 'Dimas Juancukk'

print(f"teman-teman = {teman_teman} \n")
print(f"Friends = {friends} \n")

# pop dictionary (Berdasarkan 'Key")
dataAsep = friends.pop('sep')
print(f"data Asep = {dataAsep} ")
print(f"Friends = {friends} \n")

# pop item dictionary (Berdasarkan yang Terakhir)
dataTerakhhir = friends.popitem()
print(f"data Terakhir = {dataTerakhhir} ")
print(f"Friends = {friends} \n")
