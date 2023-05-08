import numpy as np
import csv
mas1 = []
m = 12
n = 10
with open("data3.csv", encoding='utf-8') as r_file:
    reader_object = csv.reader(r_file, delimiter=';')
    for row in reader_object:
        mas1.append(list(row))
for i in range(m):
    for j in range(n):
        mas1[i][j] = float(mas1[i][j])
# метод средних арифметических рангов
def sr_znach(mas1, a):
    s = 0
    for i in range(12):
        s += mas1[i][a]
    sr = s/12
    return sr
mas_sr = []
for i in range(n):
    mas_sr.append(sr_znach(mas1, i))
def rang(mas):
    array = []
    array2 = []
    for i in range(len(mas)):
        array.append(mas[i])
        array2.append((mas[i]))
    array2.sort()
    mas_rang = []
    for j in range(len(mas)):
        for i in range(len(mas)):
            if array[i] == array2[j]:
                mas_rang.append(10-i)
            else: continue
    return mas_rang
rang1 = []
rang1.append(rang(mas_sr))
print(mas_sr, rang1)
# метод медиан
def med(mas, h):
    mas_res = []
    for i in range(12):
        mas_res.append(mas[i][h])
    mas_res.sort()
    a = mas_res[int(len(mas_res)/2)-1]
    b = mas_res[int((len(mas_res)/2))]
    if a == b:
        return a
    else: return (a+b)/2
mas_med = []
for i in range(10):
    mas_med.append(med(mas1, i))
rang2 = np.array(mas_med)
temp2 = rang2.argsort()
ranks2 = temp2.argsort()
# print(mas_med, rang2)
# Оценка степени согласованности мнений экспертов с помощью коэффициента конкордации (W)
def sr_znach2(mas1, a):
    s = 0
    for i in range(12):
        s += mas1[i][a]
    return s
sum_sr = 0
mas_otk = []
for i in range(n):
    sum_sr+=sr_znach2(mas1, i)
    mas_otk.append(sr_znach2(mas1, i))
sum_sr = sum_sr/10
for i in range(n):
    mas_otk[i] = abs(mas_otk[i]-sum_sr)
# print(sum_sr, mas_otk)
mas_otkX2 = []
for i in range(n):
    mas_otkX2.append(mas_otk[i]*mas_otk[i])
# print(mas_otkX2)
summ = sum(mas_otkX2)
print(summ)
w = (12*summ)/((m**2)*((n**3)-n))
print("w = ", w)
# Метод весовых коэффициентов
mas_koef = [0.25, 0.1, 0.1, 0, 0, 0.1, 0, 0, 0, 0.2, 0.25, 0]
for i in range(m):
    for j in range(n):
        mas1[i][j] = mas1[i][j]*mas_koef[i]
mas_sr2 = []
for i in range(n):
    mas_sr2.append(sr_znach(mas1, i))
rang3 = np.array(mas_sr2)
temp3 = rang3.argsort()
ranks3 = temp3.argsort()
print(rang1)
print(ranks2)
print(ranks3)
