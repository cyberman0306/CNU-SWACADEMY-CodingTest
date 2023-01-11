# n = int(input())
#
# for i in range(n):
#     S = input()
#     space = []
#     space2 = []
#     space = input()
#     space = list(space)
#     start, end = map(int, input().split())
#     flag = False
#
#     for j in space[start-1:end]:
#         space2.append(j)
#
#     #print(space2)
#     if len(space2) >= 3 and space2[0] == "U":
#         for p in space2[1:]:
#             if p != "m":
#                 #print(p, "gotit!")
#                 flag = False
#                 break
#             flag = True
#     if flag is False:
#         print("NO")
#     else:
#         print("YES")