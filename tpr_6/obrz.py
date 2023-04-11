import csv
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
print(mas1)
cat_dog = turtle.Turtle()
cat_dog.speed(20)
for i in range(50):
    # for j in range(4):
        cat_dog.up()
        cat_dog.setpos(mas1[i][0]*size, mas1[i][1])
        cat_dog.dot(7, "green")
        cat_dog.ht()
for i in range(50):
    # for j in range(4):
        cat_dog.up()
        cat_dog.setpos(mas1[i][2]*size, mas1[i][3])
        cat_dog.dot(7, "red")
        cat_dog.ht()
mas2 = []
mas3 = []
mas4 = []
mas5 = []
for i in range(50):
    mas2.append(mas1[i][0])
    mas3.append(mas1[i][1])
    mas4.append(mas1[i][2])
    mas5.append(mas1[i][3])
# print(mas2)
cat_dog.color("green")
cat_dog.setpos(min(mas2)*size, min(mas3))
cat_dog.down()
cat_dog.setpos(min(mas2)*size, max(mas3))
cat_dog.setpos(max(mas2)*size, max(mas3))
cat_dog.setpos(max(mas2)*size, min(mas3))
cat_dog.setpos(min(mas2)*size, min(mas3))
cat_dog.up()
cat_dog.color("red")
cat_dog.setpos(min(mas4)*size, min(mas5))
cat_dog.down()
cat_dog.setpos(min(mas4)*size, max(mas5))
cat_dog.setpos(max(mas4)*size, max(mas5))
cat_dog.setpos(max(mas4)*size, min(mas5))
cat_dog.setpos(min(mas4)*size, min(mas5))
x = float(input())
y = float(input())
if (x >= min(mas2)) and (x <= max(mas2)) and (y >= min(mas3)) and (y <= max(mas3)):
    print("Это кошка")
elif (x >= min(mas4)) and (x <= max(mas4)) and (y >= min(mas5)) and (y <= max(mas5)):
    print("Это собака")
else: print("Это условный енот, или точка отказа")
while(True):
    cat_dog.up()
    cat_dog.setpos(x*size, y)
    cat_dog.dot(7, "black")