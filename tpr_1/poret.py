import csv
mas1 = []
with open("data.csv", encoding='utf-8') as r_file:
    reader_object = csv.reader(r_file, delimiter=';')
    count = 0
    for row in reader_object:
        count+=1
        print(row)
        mas1.append(list(row))
    print(count)
mas1.pop(0)
for i in range(count-1):
    for j in range(4):
        mas1[i][j] = float(mas1[i][j])
    print(mas1[i])

mas2 = []
mas3 = [0]
for k in range(count-2):
    for l in range(1):
        # if i == j:
        #     mas3[j]=0
        #     mas2.append(mas3)
        if (mas1[k][l] > mas1[k+1][l]) or (mas1[k][l+1] > mas1[k+1][l+1]) or (mas1[k][l+2] > mas1[k+1][l+2]) or (mas1[k][l+3] > mas1[k+1][l+3]):
            mas3.append(1)
        else:
            mas3.append(0)
for i in range(count-1):
    mas2.append(mas3)
for i in range(count-1):
    print(mas2[i])

#расставить точную оценку по проекту, что это за цифры
#


