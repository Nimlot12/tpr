mas_A1 = [20, 25, 15] #вариант 8, критерий Байеса, примем общую вероятность равной 0.25
mas_A2 = [25, 24, 10]
mas_A3 = [15, 28, 12]
mas_A4 = [9, 30, 20]
mas_Bj = [mas_A1, mas_A2, mas_A3, mas_A4]
mas_res = []
V = 0.25
res = 0
print(mas_Bj)
for i in range(len(mas_Bj)):
    for j in range(3):
        res += mas_Bj[i][j] * V
    mas_res.append(res)
print(mas_res)
result = max(mas_res)
print(result)