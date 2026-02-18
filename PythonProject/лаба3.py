# import math
#
# a = float(input())
# b = float(input())
# t = float(input())
# f1 = a - (1 / (3 + math.sin(3.6 * a)))
# f2 = b - (1 / (3 + math.sin(3.6 * b)))
# x = (a * f2 - b * f1) / (f2 - f1)
# f3 = x - (1 / (3 + math.sin(3.6 * x)))
# while math.fabs(f3) > t:
#     if f1 * f3 > 0:
#         a = x
#         f1 = f3
#     else:
#         b = x
#         f2 = f3
#     x = (a * f2 - b * f1) / (f2 - f1)
#     f3 = x - (1 / (3 + math.sin(3.6 * x)))
# print('Корень х=', x)
# точность = 0.0000000000001
