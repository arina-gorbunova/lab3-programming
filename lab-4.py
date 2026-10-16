# #Задание 1
# number = int(input('введите число: '))

# if number % 2 == 0:
#     print(f"Число {number} - четное")
# else:
#     print(f"Число {number} - нечетное")


# #Дополнительное задание
# # 1. Делиться ли число на 3
# number = int(input('введите число: '))

# if number % 3 == 0:
#     print(f"Число {number} делится на 3")
# else:
#     print(f"Число {number} не делится на 3")


# # 2. Является число положительным, отрицательным или нулем
# number = int(input('введите число: '))

# if number > 0:
#     print(f"число {number} - положительное")
# elif number < 0:
#     print(f"число {number} - отрицательное")
# elif number == 0:
#     print(f"число {number} - ноль")


# #задание 2
# a = float(input("Введите перове число: "))
# b = float(input("Введите второе число: "))
# c = float(input("Введите третье число: "))

# if a >= b and a >= c:
#     maximum = a
# elif b >= a and b >= c:
#     maximum = b
# else:
#     maximum = c

# print(f"Максимум: {maximum}")


# #через функцию max()
# a = float(input("Введите перове число: "))
# b = float(input("Введите второе число: "))
# c = float(input("Введите третье число: "))

# print(f"Максимум: {max(a, b, c)}")


# #задание 3
# age = int(input('Введите возраст: '))

# if age < 0:
#     print('Некорректный возраст')
# elif age <= 12:
#     print("Ребенок")
# elif age <= 17:
#     print("Подросток")
# elif age <= 64:
#     print("Взрослый")
# else:
#     print("Пожилой")



# #задание 4
# import math

# a = float(input("Введите a: "))
# b = float(input("Введите b: "))
# c = float(input("Введите c: "))

# if a == 0:
#     print("Это не квадратное уравнение")
# else:
#     D = b**2 - 4*a*c

# if D > 0:
#     x1 = (-b + math.sqrt(D)) / 2*a
#     x2 = (-b - math.sqrt(D)) / 2*a
#     print(f"Два корня: x1 = {x1:.2f}, x2 = {x2:.2f}")
# elif D == 0:
#     x = -b/2*a
#     print(f"Один корень: x = {x:.2f}")
# else:
#     print("Нет действительных корней")



# #задание 5
# a = float(input("Ваедите первое число: "))
# b = float(input("Ваедите второе число: "))
# operation = input("Введите операцию (+, -, *, /): ").strip()

# match operation:
#     case "+":
#         print(f"Результат: {a + b}")
#     case "-":
#         print(f"Результат: {a - b}")
#     case "*":
#         print(f"Результат: {a * b}")
#     case "/":
#         if b == 0:
#             print("Ошибка: деление на ноль!")
#         else:
#             print(f"Результат: {a / b:.2f}")
#     case _:
#         print("Неизвестная операция")


# #задание 6
# year = int(input("Введите год: "))

# if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#     print(f"{year} - високосный год")
# else:
#     print(f"{year} - не високосный год")




#задание 7
a = float(input("Введите сторону a: "))
b = float(input("Введите сторону b: "))
c = float(input("Введите сторону c: "))

if a + b > c and a + c > b and b + c > a:
    if a == b == c:
        print("Равносторонний треугольник")
    elif a == b or b == c or a == c:
        print("Равнобедренный треугольник")
    else:
        print("Разносторонний треугольник")
else:
    print("Треугольник не существует")