mas_A1 = [20, 25, 15] #вариант 8, критерий Гурвица A*max(i) + (1-A)min(i), где А степень оптимизма от 0 до 1
mas_A2 = [25, 24, 10]            #Для данного примера возьмем А = 0,6
mas_A3 = [15, 28, 12]
mas_A4 = [9, 30, 20]
A = 0.6
mas_Bj = [mas_A1, mas_A2, mas_A3, mas_A4]
mas_res = []
print(mas_Bj)
for i in range(len(mas_Bj)):
    a1 = max(mas_Bj[i])
    a2 = min(mas_Bj[i])
    mas_res.append(A*a1+(1-A)*a2)
print(mas_res)
result = max(mas_res)
print(result)