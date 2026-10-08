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



# total_seconds = int(input("Введите количество секунд: "))

# hours = total_seconds // 3600
# minutes = (total_seconds % 3600) // 60
# seconds = total_seconds % 60

# print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")



# text = input("Введите строку: ")

# print(f"Длина: {len(text)}")
# print(f"Верхний регистр: {text.upper()}")
# print(f"Нижний регистр: {text.lower()}")
# print(f"Первый символ: {text[0]}")
# print(f"Последний символ: {text[-1]}")
# print(f"Количество пробелов: {text.count(' ')}")



# a = float(input("Введите первое число: "))
# b = float(input("Введите второе число: "))
# c = float(input("Введите третье число: "))

# average = (a + b + c) / 3
# minimum = min(a, b, c)
# maximum = max(a, b, c)

# print(f"Среднее арифметическое: {average:.2f}")
# print(f"Минимум: {minimum}")
# print(f"Максимум: {maximum}")




# print("Конвертер температур")
# print("1. Из °C в °F")
# print("2. Из °F в °C")

# choice = input("Ваш выбор (1/2): ")

# if choice == "1":
#     celsius = float(input("Введите температуру в °C: "))
#     fahrenheit = celsius * 9/5 + 32
#     print(f"{celsius:.1f}°C = {fahrenheit:.1f}°F")
# elif choice == "2":
#     fahrenheit = float(input("Введите температуру в °F: "))
#     celsius = (fahrenheit - 32) * 5/9
#     print(f"{fahrenheit:.1f}°F = {celsius:.1f}°C")
# else:
#     print("Некорректный выбор") 



def tobinary(num_10):
    num_10 = abs(num_10) # работаем с модулем, чтобы обрабатывать и отрицательные числа
    if num_10 == 0:
        return "0"
    num_2 = ""
    while num_10 != 0:
        ost = str(num_10 % 2) # остаток от деления(0 или 1)
        num_2 = ost + num_2 # приписываем слева
        num_10 //= 2 # целочисленно делим число
    return num_2

def main():
    try:
        num_10 = int(input("Введите число в 10 сс:")) # запрос ввода числа в 10-тичной сс

        # ЧЕРЕЗ ФУНКЦИЮ bin()
        num_2bin = bin(num_10)[2:] # [2:] нужен, чтобы убрать префикс '0b'

        # ВРУЧНУЮ
        num_2 = tobinary(num_10)

        # ВЫВОДЫ
        print(f"Десятичное число {num_10} в двоичной сс равно {num_2bin}(через функцию bin)")
        print(f"Десятичное число {num_10} в двоичной сс равно {num_2}(вручную)")

    except ValueError:
        print("Ошибка: нужно ввести именно целое число!!!!")
if __name__ == "__main__":
    main()