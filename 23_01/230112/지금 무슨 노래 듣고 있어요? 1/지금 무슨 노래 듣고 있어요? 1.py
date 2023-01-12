n = int(input())

space_name = []
space_dict = {}
space_sec = []
space_play = []
sec = []
for _ in range(n):
    space_name.append(input())
for i in range(n):
    space_dict[space_name[i]] = int(input())
for i in range(n):
    space_sec.append(space_dict[space_name[i]])
for i in range(n):
    if i == 0:
        space_play.append(space_sec[0])
    else:
        space_play.append(space_play[i-1]+space_sec[i])



#print(space_sec)
#print(space_play)

count = int(input())
for _ in range(count):
    temp = int(input())
    sec.append(temp)
#print(sec)

for j in sec:
    for i in space_play:
        if j <= i:
            # print(j)
            # print(i)
            print(space_name[space_play.index(i)])
            break
        # else:
        #     print("not in")
        #     print(j)
        #     print(i)
        #     print()



#print(space_dict['Hype Boy'])
