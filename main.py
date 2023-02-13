import sains.matematika
from sains import fisika
from sains.fisika import gaya as force

hasil_tambah = sains.matematika.tambah(1, 4, 5, 6, 7)
print(f"hasil tambah dari package sains = {hasil_tambah} ")

gaya = fisika.gaya(90, 10)

print(f"gaya adalah = {gaya} ")
gaya = force(90, 10)

print(f"gaya adalah = {gaya} ")
