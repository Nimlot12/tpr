# порог разбиения 0.5
exp1 = [2, 8, 1, 5, 3, 6, 9, 10, 4, 7]
exp2 = [1, 5, 3, 2, 8, 6, 9, 7, 4, 10]
exp3 = [2, 8, 1, 3, 5, 10, 7, 4, 6, 9]
exp4 = [5, 8, 1, 2, 3, 7, 4, 6, 10, 9]
exp5 = [8, 2, 1, 5, 3, 6, 9, 4, 10, 7]
exp6 = [2, 8, 5, 1, 3, 4, 10, 7, 9, 6]
exp7 = [8, 3, 1, 2, 5, 4, 7, 10, 9, 6]
exp8 = [5, 1, 3, 2, 8, 7, 4, 6, 10, 9]
exp9 = [5, 3, 1, 8, 2, 4, 10, 7, 6, 9]
exp10 = [2, 3, 1, 5, 8, 4, 6, 7, 10, 9]
exp11 = [2, 8, 1, 5, 3, 6, 9, 4, 10, 7]
exp12 = [5, 3, 1, 2, 8, 4, 6, 7, 10, 9]
eo = [exp1, exp2, exp3, exp4, exp5, exp6, exp7, exp8, exp9, exp10, exp11, exp12]


def srv(eo, a, b):
    mas1 = []
    for i in range(12):
        for j in range(10):
            if a == i:
                if eo[i][j] == eo[b][j]:
                    mas1.append(1)
                if eo[i][j] != eo[b][j]:
                    mas1.append(0)
    return mas1


def srv2(mas_res, b, eo, a):
    for i in range(len(eo)):
        mas_res.append(srv(eo, a, b))
        b += 1
    return mas_res

porog = 0.5
b = 0
a = 0
array = []
mas_sum = []
mas_sum1 = []
for i in range(12):
    mas_res = []
    array.append(srv2(mas_res, b, eo, a))
    a += 1
for i in range(12):
    for j in range(12):
        a = 0
        for k in range(10):
            a += array[i][j][k]
        mas_sum1.append(a)
    mas_sum.append(mas_sum1)
    mas_sum1 = []
for i in range(12):
    for j in range(12):
        mas_sum[i][j] = mas_sum[i][j]/10
mas_porog = []
for i in range(12):
    mas_porog1 = []
    for j in range(12):
        if mas_sum[i][j] >= porog:
            mas_porog1.append(1)
        else:
            mas_porog1.append(0)
    mas_porog.append(mas_porog1)
groups = []
for i in range(12):
    group = []
    for j in range(12):
        if mas_porog[i][j] == 1:
            group.append(j+1)
    groups.append(group)
for i in range(12):
    print(*mas_porog[i])
print(groups)

