# Введите 3 числа, найдите произведение чисел

# first_number = int(input("Введите первое число:  "))
# second_number = int(input("Введите второе число:  "))
# print(first_number * second_number)

# Типы данных
# a = "Привет"
# print(type(a))

# b = 4
# print(type(b))

# c = 4.65
# print(type(c))

# d = True
# print(type(d))

# number = int(input('Введите число: '))
# if number>0:
#     print(f'Число {number} положительное')
#     if number !=10:
#         print(f'Число {number} положительное и не равно 10')
# elif number == 0:
#     print('Ноль')
# else:
#     print(f'Число {number} отрицательное')

# a = 10
# b = 3
# print(a+b)
# print(a-b)
# print(a*b)
# print(a/b)
# print(a//b)
# print(a%b)
# print(a**b)


# Пользователь вводит целое число. Выведите Yes, если это число четырехзначное,
# и No в противном случае

# a = int(input('Введите число: '))
# if (a>999) and (a<10000):
#     print(f'Число {a} четырехзначное')
# else:
#     print(f'Число {a} не четырехзначное')


# Введите целое число.
# Выведите его строку - описание вида "отрицательное четное число", "ноль",
"положительное целое число"
# Например, численным описанием числа 190 является срока "положительное целое число"

# a = int(input("Введите число: "))
# if a>0 and a%2==0:
#     print(f"Число {a} положительное четное")
# elif a==0:
#     print(f"Число {a} ноль")
# elif a<0 and a%2==0:
#     print (f"Число {a} отрицательное четное")
# elif a<0 and a%2!=0:
#     print (f"Число {a} отрицательное нечетное")
# elif a<0 and a%2!=0:
#     print (f"Число {a} отрицательное нечетное")
# else:
#     print("Не подпадает ни под один параметр")

# За день машина проезжает n километров.
# Сколько дней нужно, чтобы проехать маршрут длиной в m километров?

# n = float(input("Введите количество километров за день: "))
# m = float(input("Введите количество километров в маршруте: "))

# print (int(((m-0.1)//n)+1))


# В некоторой школе решили набрать три новых
# математических класса и оборудовать кабинеты для
# них новыми партами. За каждой партой может сидеть
# два учащихся. Известно количество учащихся в
# каждом из трех классов. Выведите наименьшее
# число парт, которое нужно приобрести для них.


# a = int(input("Введите количество учеников в 1 классе "))
# b = int(input("Введите количество учеников во 2 классе "))
# c = int(input("Введите количество учеников в 3 классе "))

# print(int(((a // 2) + a % 2) + ((b // 2) + b % 2) + ((c // 2) + c % 2)))


# Дано натуральное число. Требуется определить,
# является ли год с данным номером високосным. Если
# год является високосным, то выведите YES, иначе
# выведите NO. Напомним, что в соответствии с
# григорианским календарем, год является
# високосным, если его номер кратен 4, но не кратен
# 100, а также если он кратен 400.


# a = int(input("Введите год: "))
# if ((a % 4 == 0) and (a % 100 != 0)) or (a & 400 == 0):
#     print(f"Год {a} високосный")
# else:
#     print(f"Год {a} не високосный")


# Задача 2: Найдите сумму цифр трехзначного числа.
#
# *Пример:*
#
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

# number = int(input("Введите трехзначное число:  "))
# print(int(number//100)+(number//10%10)+(number%10))

# Задача 4
# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
# Пример:
# 6 -> 1 4 1
# 24 -> 4 16 4
# 60 -> 10 40 10

# number = 12
# print("Петя и Сережа сделали по" ,number/4, "журавликов, а Катя сделала" ,number/2, "журавликов")


# Задача 6
# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
# Пример:
# 385916 -> yes
# 123456 -> no

# ticket_number = input('Введите шестизначный номер билета: ')
# a = int(ticket_number[0]) + int(ticket_number[1]) + int(ticket_number[2])
# b = int(ticket_number[3]) + int(ticket_number[4]) + int(ticket_number[5])
# if a == b:
#     print('Билет счастливый!')
# else:
#     print('Билет не счастливый(')


# Задача 8.
# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

# a,b,c = int(input('Введите 1-ю сторону: ')),int(input('Введите 2-ю сторону: ')),int(input('Введите кол-во долек: '))
# if c%a == 0 or c%b == 0:
#     print('Можно отломить')
# else: print('Нельзя отломить')