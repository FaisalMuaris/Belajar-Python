# module matematika dengan import

from moduleMatematika import tambah as add
from moduleMatematika import kali as k
from moduleMatematika import pangkat as p
# from moduleMatematika *

import moduleMatematika as math  # <-- bisa dilakukan

hasil_tambah = add(24, 525, 1)
print(f"hasil tambah = {hasil_tambah } ")

hasil_kali = math.kali(24, 525, 1)
print(f"hasil kali = {hasil_kali } ")

pangkat_3 = p(3)
print(f"hasil pangkat 3 = {pangkat_3(3)} ")
