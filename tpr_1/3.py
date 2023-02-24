#субоптимизация
#основной критерий озу, т.е. f2
import csv
mas1 = []
with open("data.csv", encoding='utf-8') as r_file:
    reader_object = csv.reader(r_file, delimiter=';')
    count = 0
    for row in reader_object:
        count+=1
        mas1.append(list(row))
mas1.pop(0)
for i in range(count-1):
    for j in range(4):
        mas1[i][j] = float(mas1[i][j])
mas_res=[]
for i in range(count-1):
    for j in range(1):
        if (mas1[i][j] == 0.0) and (mas1[i][j+2] >= 7.0) and (mas1[i][j+3] <= 2.0):
            mas_res.append(mas1[i][j+1])
max = 0
for i in range(len(mas_res)):
    if max < mas_res[i]:
        max = mas_res[i]
for i in range(count-1):
    for j in range(1):
        if (mas1[i][j] == 0.0) and (mas1[i][j+2] >= 7.0) and (mas1[i][j+3] <= 2.0) and (mas1[i][j+1] == max):
            print(i+1)