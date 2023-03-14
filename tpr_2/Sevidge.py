mas_A1 = [20, 25, 15] #вариант 8, критерий Сэвиджа min(max(ai))
mas_A2 = [25, 24, 10]
mas_A3 = [15, 28, 12]
mas_A4 = [9, 30, 20]
mas_Bj = [mas_A1, mas_A2, mas_A3, mas_A4]
mas_res = []
print(mas_Bj)
for i in range(len(mas_Bj)):
    mas_res.append(max(mas_Bj[i]))
print(mas_res)
result = min(mas_res)
print(result)