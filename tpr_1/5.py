#построение обобщенного критерия
# f1 = 0.2, f2 = 0.4, f3 = 0.2, f4 = 0.2
# первый критерий взял на максимум в отличии от других пунктов, иначе дальше будет деление на ноль, соответственно
# ответ будет отличатсья от других пунктов
import csv
mas1 = []
with open("data.csv", encoding='utf-8') as r_file:
    reader_object = csv.reader(r_file, delimiter=';')
    count = 0
    for row in reader_object:
        count+=1
        mas1.append(list(row))
mas1.pop(0)
mas2 = []
mas3 = []
mas4 = []
mas5 = []
v1 = 0.2
v2 = 0.4
v3 = 0.2
v4 = 0.2
for i in range(count-1):
    for j in range(4):
        mas1[i][j] = float(mas1[i][j])
for i in range(count-1):
    for j in range(1):
        mas2.append(mas1[i][j])
        mas3.append(mas1[i][j+1])
        mas4.append(mas1[i][j+2])
        mas5.append(mas1[i][j+3])
max1 = max(mas2)
max2 = max(mas3)
max3 = max(mas4)
max4 = max(mas5)
for i in range(count-1):
    for j in range(1):
        mas1[i][j] = mas1[i][j]/max1
        mas1[i][j+1] = mas1[i][j+1] / max2
        mas1[i][j+2] = mas1[i][j+2] / max3
        mas1[i][j+3] = mas1[i][j+3] / max4
print(mas1)
mas_res = []
for i in range(count-1):
    for j in range(1):
        mas_res.append(mas1[i][j]*v1+mas1[i][j+1]*v2+mas1[i][j+2]*v3+mas1[i][j+3]*v4)
max_result = max(mas_res)
for i in range(len(mas_res)):
    if mas_res[i]==max_result:
        print(i+1)
