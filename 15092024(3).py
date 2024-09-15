print("введите разные координаты вершин точек")
print("введите первую точку")
x1 = float(input("X: "))
y1 = float(input("Y: "))

print("введите вторую точку")
x2 = float(input("X: "))
y2 = float(input("Y: "))

print("введите третью точку")
x3 = float(input("X: "))
y3 = float(input("X: "))

print("3 точки могут образовать треугольник")

a = ((x1 - x2)** 2) + ((y1 - y2)** 2)
print("длина стороны a")
print(a)

b = ((x2 - x3)** 2) + ((y2 - y3)** 2)
print("длина стороны b")
print(b)

c = ((x3 - x1)** 2) + ((y3 - y1)** 2)
print("длина стороны c")
print(c)

if a == b == c:
    print("равносторонний")
elif a == b:
    print("равнобедренный")
elif b == c:
    print("равнобедренный")
elif a == c:
    print("равнобедренный")
else:
    print("разносторонний")