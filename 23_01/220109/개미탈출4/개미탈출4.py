#
# def battle(ATK_J, HP_J, ATK_M, HP_M, list):
#     while True:
#         HP_M -= ATK_J
#         HP_J -= ATK_M
#         if HP_M <= 0:
#             list.remove("&")
#             return list
#         elif HP_J <= 0:
#             return list
# junsik = "@"
# monster = "&"
# wall = "#"
# exit = "O"
# n = int(input())
# for i in range(n):
#     space = []
#     length, crash = map(int, input().split())
#     space = input()
#     space = list(space)
#     # arrange_list(space) #콤마 삭제
#     ATK_J, HP_J = map(int, input().split())
#     ATK_M, HP_M = map(int, input().split())
#     battle(ATK_J, HP_J, ATK_M, HP_M, space) # 몬스터 삭제
#     junsik_index = space.index("@")
#     length = len(space)
#     last_index = length -1
#     space2 = []
#     space3 = []
#     for j in space[junsik_index + 1: ]:
#         space2.append(j)
#         if j == exit:
#             break
#     #print()
#     #print("right")
#     #print(space2)
#     for j in reversed(space[0:junsik_index]):
#         space3.append(j)
#         if j == exit:
#             break
#     #print("left")
#     #print(space3)
#     if exit in space2:
#         for k in range(crash):
#             if wall in space2:
#                 space2.remove(wall)
#                 #print("right removed!")
#         #print(crash, "right", space2)
#         if monster not in space2 and wall not in space2:
#             a = 1
#         else:
#             a = 0
#     else:
#         a = 0
#     if exit in space3:
#         for g in range(crash):
#             if wall in space3:
#                 space3.remove(wall)
#                 #print("left removed!")
#         #print(crash, "left", space3)
#         if wall not in space3 and monster not in space3:
#             b = 1
#         else:
#             b = 0
#     else:
#         b = 0
#     if a == 1 or b == 1:
#         print("HAHA!")
#     else:
#         print("HELP!")
