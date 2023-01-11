
# import sys
# input = sys.stdin.readline
# import decimal
#
# context = decimal.getcontext()
# context.rounding = decimal.ROUND_HALF_UP
#
# for _ in range(int(input())):
#     n, u = input().split()
#     if u == 'K':
#         answer = float(n) / 1.6
#         answer = round(decimal.Decimal(answer), 2)
#         if str(answer)[-1] == '0':
#             print(float(str(answer)[:-1]))
#         else:
#             print(answer)
#     else:
#         answer = float(n) * 1.6
#         answer = round(decimal.Decimal(answer), 2)
#         if str(answer)[-1] == '0':
#             print(float(str(answer)[:-1]))
#         else:
#             print(answer)

#
# import decimal
#
# context = decimal.getcontext()
# context.rounding = decimal.ROUND_HALF_UP
#
# print(round(decimal.Decimal('2.5'), 0))  # 3