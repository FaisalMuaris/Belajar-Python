import io
from collections import Counter
import datetime as dt

data_waktu = dt.datetime.now()

print(f"datetime now = {data_waktu} ")

print(f"tahun : {data_waktu.year} ")
print(f"Hari : {data_waktu.strftime('%A')} ")


data = ['a', 'b', 'c', 'b', 'e']
data_count = Counter(data)
# count = 0
# for i in data:
#     if i == 'b':
#         count += 1

# print(count)


print(f"data count = {data_count} ")
print(f"jumlah a = {data_count['a']} ")
print(f"jumlah b = {data_count['b']} ")


file = io.open("file_text.txt", "r")
print(file.read())
