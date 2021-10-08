print("Введите коэффициенты для уравнения")
print("ax^2 + bx + c = 0:")

a = float(input("a = "))
b = float(input("b = "))
c = float(input("c = "))

Discrim = b ** 2 - 4 * a * c
print("Дискриминант D = ", Discrim)

if Discrim > 0:
    x1 = (-b + Discrim ** (0.5)) / (2 * a)
    x2 = (-b - Discrim ** (0.5)) / (2 * a)
    print("x1 = ", x1, "   ", "х2 = ", x2)
elif Discrim == 0:
    x = (-b / (2 * a))
    print("x= ", x)
else:
    print("Корней нет")
