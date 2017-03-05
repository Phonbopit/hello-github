# s[start:stop:how to count]

s[::-1]  # reverse

print('{:>3}'.format(), end="")
print('{:,}'.format(), end="")
print('{:20}'.format(), end="")  # เติม space ข้างซ้ายจนกว่าจะครบ 20
print('{:=20}'.format(), end="")  # เติม space ข้างซ้ายจนกว่าจะครบ 20

for i, e in enumerate(foo):
    pass
while n != q:
    pass

list  # []
.append(information)
.clear()
.insert(index, information)
"".join(arg)
# a = [cause1 if check1 else cause2 for something]
# a = [ cause1 for something if check1 ] for discard invalid

set  # {}
|  # union
&  # intersec
a - b  # in a not in b
a ^ b  # a | b - intersec
.add(1arg)
.update({**arg})
.remove()
.discard()  # no error

zip  # รวม list หรือ tuple หลายๆตัวเข้าด้วยกัน
itertools
cycle

dict
d[key] = value
del
.keys.values.items
dict
comprehension
d1 = {k: v for k, v in t}

with open('fx.txt') as f:
    d = {line[0]: line[:-1] for line in f}
    s = f.readlines() # อ่านข้อมูลมาอยู่ใน list
    s = f.strip()
    s = [line.strip() for line in f]

with open(,encoding=utf8)
def read_f():
    with open('r"c:/fx.txt') as f:
        for line in f:
            s = line.split(',')
        print(s)

import csv
    data = csv.reader(file) # = list of string
    data = csv.DictReader(file) # read file header
    print(data.fieldnames)
    fw=csv.writer
    fw.writerow(file)

import datetime
dt = datetime.datetime.now().strftime('%y %m %d %h:%m:%s')

import urllib.request

with urllib.request.urlopen(link)as f:
    pass

import pyuca #unicode c algorhythm
sorted(file,key = pyuca.Collator().sort_key

from collections import Counter


od = Orderdict()

a = vars()
create dict attributes
attrs =
s =[ %% getattr(self,a) for a in attrs]

@property
def blood(self):
    return self.__blood

@blood.setter
def blood(self, blood):
    if blood.upper() in ["A", "B", "AB", "O"]:
        self.__blood = blood.upper()

ExchangeRate.__fx #class level attr

@classmethod
new way to create constructor

from abc import ABC

@abstractmethod
def foo():
    pass