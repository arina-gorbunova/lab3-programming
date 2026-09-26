#Лабораторная 3
# Запрос данных
# integer = int(input("Введите целое число: "))
# decimal = float(input("Введите дробное число: "))
# text = input("Введите строку: ")

# # Вывод типов и значений.
# print(f"Значение: {integer}, тип: {type(integer).__name__}")
# print(f"Значение: {decimal}, тип: {type(decimal).__name__}")
# print(f"Значение: {text}, тип: {type(text).__name__}") 


# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))

# print(f"Сумма: {a + b}")
# print(f"Разность: {a - b}")
# print(f"Произведение: {a * b}")
# print(f"Деление: {a / b:.2f}")
# print(f"Целочисленное деление: {a // b}")
# print(f"Остаток: {a % b}")
# print(f"Степень: {a ** b:.2f}") 



total_seconds = int(input("Введите количество секунд: "))

hours = total_seconds // 3600
minutes = (total_seconds % 3600) // 60
seconds = total_seconds % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")