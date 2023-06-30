import os
os.system("cls")

import datetime

data_waktu = datetime.datetime.now() 
print(f"datetime now = {data_waktu}")
print(f"tahun : {data_waktu.year}")
print(f"hari : {data_waktu.strftime('%A')}")

from collections import Counter

data = ["a", "b", "c", "d","a", "c", "b", "e", "c"]

data_count = Counter(data)
print(data_count)
print(f"data count {data_count}")
print(f"jumlah a = {data_count['a']}")
print(f"jumlah d = {data_count['d']}")
print(f"jumlah c = {data_count['c']}")

import io

file = io.open("file_text.txt", "r")
print(file.read())