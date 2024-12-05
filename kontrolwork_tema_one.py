#контрольная работа номер 1
#Козлов Михаил х-72
#задание 1(zadanie 1)
# length=int(input("Введите длину(в нанометрах):"))
# width=int(input("Введите ширину(в нанометрах):"))
# s=length * width
# print('площадь моллекулы:',s,"нанометров")
#2 задание(zadanie 2)
# Cм=int(input("Введите молярную концентрацию:"))
# V=int(input("Введите объем(в литрах):"))
# Na=6.022 #* 10**23
# N=Cм / V * Na
# print(N,'* 10**23')
#3 задание(3 zadanie)
import math

def calculate_factorial(n):
    if n < 0:
        raise ValueError("Факториал не определен для отрицательных чисел")
    return math.factorial(n)

# Пример использования
try:
    number = int(input("Введите число для вычисления факториала: "))
    print(f"Факториал {number} равен {calculate_factorial(number)}")
except ValueError as e:
    print(e)




