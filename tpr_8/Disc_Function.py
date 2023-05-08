import csv
import numpy
import turtle
mas1 = []
size = 13
with open("data2.csv", encoding='utf-8') as r_file:
    reader_object = csv.reader(r_file, delimiter=';')
    for row in reader_object:
        mas1.append(list(row))
for i in range(50):
    for j in range(4):
        mas1[i][j] = float(mas1[i][j])
# print(mas1)
cat_dog = turtle.Turtle()
cat_dog.speed(20)
for i in range(50):
        cat_dog.up()
        cat_dog.setpos(mas1[i][0]*size, mas1[i][1])
        cat_dog.dot(7, "green")
        cat_dog.ht()
for i in range(50):
        cat_dog.up()
        cat_dog.setpos(mas1[i][2]*size, mas1[i][3])
        cat_dog.dot(7, "red")
        cat_dog.ht()
mas_srX1, mas_srX2, mas_srY1, mas_srY2, mas_Xi_M1, mas_Yi_M1, mas_Xi_M2, mas_Yi_M2 = [], [], [], [], [], [], [], []
for i in range(len(mas1)):
    mas_srX1.append(mas1[i][0])
    mas_srX2.append(mas1[i][2])
    mas_srY1.append(mas1[i][1])
    mas_srY2.append(mas1[i][3])
# print(mas_srX1, mas_srX2, mas_srY1, mas_srY2)
MX1 = numpy.average(mas_srX1)
MX2 = numpy.average(mas_srX2)
MY1 = numpy.average(mas_srY1)
MY2 = numpy.average(mas_srY2)
# print(MX1, MX2, MY1, MY2)
for i in range(len(mas1)):
    mas_Xi_M1.append(mas_srX1[i]-MX1)
    mas_Xi_M2.append(mas_srX2[i] - MX2)
    mas_Yi_M1.append(mas_srY1[i] - MY1)
    mas_Yi_M2.append(mas_srY2[i] - MY2)
# print(mas_Xi_M1, mas_Yi_M1, mas_Xi_M2, mas_Yi_M2)
mas_1_2_1, mas_1_2_2, mas_1_1_1, mas_1_1_2, mas_2_2_1, mas_2_2_2 = [], [], [], [], [], []
for i in range(len(mas1)):
    mas_1_2_1.append(mas_Xi_M1[i] * mas_Yi_M1[i])
    mas_1_2_2.append(mas_Xi_M2[i] * mas_Yi_M2[i])
    mas_1_1_1.append(mas_Xi_M1[i] * mas_Xi_M1[i])
    mas_1_1_2.append(mas_Xi_M2[i] * mas_Xi_M2[i])
    mas_2_2_1.append(mas_Yi_M1[i] * mas_Yi_M1[i])
    mas_2_2_2.append(mas_Yi_M2[i] * mas_Yi_M2[i])
# print(mas_1_2_1, mas_1_2_2, mas_1_1_1, mas_1_1_2, mas_2_2_1, mas_2_2_2)
SR121 = numpy.average(mas_1_2_1)
SR122 = numpy.average(mas_1_2_2)
SR111 = numpy.average(mas_1_1_1)
SR112 = numpy.average(mas_1_1_2)
SR221 = numpy.average(mas_2_2_1)
SR222 = numpy.average(mas_2_2_2)
# print(SR121, SR122, SR111, SR112, SR221, SR222)
matrix1 = numpy.matrix([[SR111, SR121], [SR121, SR221]])
matrix2 = numpy.matrix([[SR112, SR122], [SR122, SR222]])
matrix_E = (50*matrix1+50*matrix2)/100
matrix_E_1 = numpy.linalg.inv(matrix_E)
# print(matrix_E_1)
Madd = numpy.matrix([[MX1+MX2, MY1+MY2]])
Mpop = numpy.matrix([[MX1-MX2], [MY1-MY2]])
b = matrix_E_1.dot(Mpop)
p = (-0.5*(Madd.dot(b)))
# print(p)
b1 = float(b[0])
b2 = float(b[1])
# print(b1, b2)
def Y(x, p, b1, b2):
    y = (-p-b1*x)/b2
    return y
x1 = float(input())
x2 = float(input())
y1 = float(Y(x1, p, b1, b2))
y2 = float(Y(x2, p, b1, b2))
print(y1, y2)
cat_dog.up()
cat_dog.setpos(x1*size, y1)
cat_dog.color('grey')
cat_dog.down()
cat_dog.setpos(x2*size, y2)

def Opr(x, y):
    if (y > Y(x, p, b1, b2)):
        print("Это собака")
    elif (y < Y(x, p, b1, b2)):
        print("Это кошка")
    else: print("Это условный енот, или точка отказа")
    cat_dog.up()
    cat_dog.setpos(x*size, y)
    cat_dog.dot(7, "black")
while(True):
    x = float(input())
    y = float(input())
    Opr(x, y)
