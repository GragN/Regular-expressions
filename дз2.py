import re
from pprint import pprint
import csv

filename = "phonebook_raw.csv"
with open(filename, "r", encoding="utf-8") as f:
  rows = csv.reader(f)
  contacts_list = list(rows)
print(contacts_list)

new_list1 = list()
for i in contacts_list:
    row = ",".join(i)
    pattern = r"(\+?)(\d{1})(\s?)(\(?)(\d{3})(\)?)(.?)(\d{3})(.?)(\d{2})(.?)(\d{2})(\s?)(\(?)(\доб.)?(\s?)(\d{4})?(\)?)"
    sub = r"+7(\5)\8-\10-\12 \15\17"
    result = re.sub(pattern, sub, row)
    new_list1.append(result.split(","))

new_list2 = list()
for i in new_list1:
    row = ",".join(i)
    pattern = r"([А-Я])([а-я]+)(.)([А-Я])([а-я]+)(.)(\,)?(\,)?(\,)?([А-Я])?([а-я]+)?(\W)+"
    sub = r"\1\2,\4\5,\10\11,\7\8\9"
    result = re.sub(pattern, sub, row)
    new_list2.append(result.split(","))

new_list3 = list()
new_list4 = list()
for id, i in enumerate(new_list2):
    if i[0] not in new_list3:
        new_list3.append(i[0])
    else:
        new_list4.append(i[0])

set1 = set(new_list3)
set2 = set(new_list4)
set3 = set1.symmetric_difference(set2)
new_list5 = list(set3)

new_list6 = list()
new_list7 = list()
for i in new_list2:
    if i[0] not in new_list5:
        new_list6.append(i)
    else:
        new_list7.append(i)

for id, i in enumerate(new_list6):
    pass

constant = 0
constant1 = 1
new_list8 = list()
while constant1 <= (id):
    new_list9 = list()
    if new_list6[constant][0] == new_list6[constant1][0]:
        for i, j in zip(new_list6[constant], new_list6[constant1]):
            if i == j:
                new_list9.append(i)
            elif i == "":
                new_list9.append(j)
            elif j == "":
                new_list9.append(i)
        new_list8.append(new_list9)
        constant += 1
        constant1 += 1
    elif new_list6[constant][0] != new_list6[constant1][0]:
        constant += 1
        constant1 += 1

for i in new_list8:
    new_list7.append(i)

filename = "new_phonebook_raw.csv"
with open(filename, "w", encoding="utf-8", newline="") as f:
  writer = csv.writer(f, delimiter=",")
  writer.writerows(new_list7)