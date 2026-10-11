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



#задание 2
a = float(input("Введите перове число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

if a >= b and a >= c:
    maximum = a
elif b >= a and b >= c:
    maximum = b
else:
    maximum = c

print(f"Максимум: {maximum}")


#через функцию max()
a = float(input("Введите перове число: "))
b = float(input("Введите второе число: "))
c = float(input("Введите третье число: "))

print(f"Максимум: {max(a, b, c)}")