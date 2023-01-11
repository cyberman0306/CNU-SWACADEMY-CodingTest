# def checker(space, answer):
#     if len(space) >= 3 and space[0] == "U" and space.count("U") == 1:
#         answer += 1
#         return answer
#     elif len(space) < 3 or "U" not in space or space.count("m") < 2:
#         return answer
#     else:
#         space.remove(space[0])
#         checker(space, answer)
#     return answer
#
#
# n = int(input())
# for i in range(n):
#     length, count = map(int, input().split())
#     space = []
#     space2 = []
#     space = input()
#     space = list(space)
#     answer = 0
#     for j in range(count):
#         space2 = []
#         a, b = map(int, input().split())
#         answer = checker(space[a - 1:b], answer)
#     print(answer)
