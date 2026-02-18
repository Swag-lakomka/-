# import math
#
# for i in range(-3, 51):
#     print('Введите x из диапазона [-3, 50]')
#     x = float(input())
#     if x <= 0:
#         print(2 ** (x + 2) + 3 * math.cos(x))
#     elif 0 < x <= 1:
#         print(x ** 3 + x - 2)
#     elif 1 < x <= 50:
#         print(math.sqrt(abs(x - 1 + x ** (2 * x + 1))))
#     else:
#         print('Функция не определена')