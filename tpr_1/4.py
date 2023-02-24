#Лексикографическая оптимизация
# 1 приоритет оперативная память, т.е. f2
# 2 приоритет дискретная видеокарта, т.е. f1
# 3 приоритет работа от аккумулятора, т.е. f3
# 4 приоритет вес, т.е. f4
import csv
mas1 = []
with open("data.csv", encoding='utf-8') as r_file:
    reader_object = csv.reader(r_file, delimiter=';')
    count = 0
    for row in reader_object:
        count+=1
        mas1.append(list(row))
mas1.pop(0)
mas_res = []
for i in range(count-1):
    for j in range(4):
        mas1[i][j] = float(mas1[i][j])
for i in range(count-1):
    for j in range(1):
        mas_res.append(mas1[i][j+1])
max = max(mas_res)
count2 = 0
for i in range(count-1):
    if(mas_res[i]==max):
        count2+=1
if count2==1:
    for i in range(len(mas_res)):
        if mas_res[i] == max:
            print(i)
else:
    mas_res1 = []
    for i in range(count - 1):
        for j in range(1):
            if mas_res[i] == max:
                mas_res1.append(mas1[i][j])
    min = min(mas_res1)
    count3 = 0
    for i in range(len(mas_res1)):
        if (mas_res1[i] == min):
            count3 += 1
    if count3 == 1:
        for i in range(count-1):
            for j in range(1):
                if (mas1[i][j] == min) and (mas1[i][j+1] == max):
                    print(i+1)
    # else:
    #     mas_res2 = []
    #     for i in range(count-1):
    #         for j in range(1):
    #             if mas_res1[i] == min:
    #                 mas_res1.append(mas1[i][j])
    #     max1 = min(mas_res1)
    #     count3 = 0
    #     for i in range(len(mas_res1)):
    #         if (mas_res1[i] == min):
    #             count3 += 1
    #     if count3 == 1:
    #         for i in range(len(mas_res1)):
    #             if mas_res1[i] == min:
    #                 print(i)

