import sys
input = sys.stdin.readline().rstrip

ans = input()
ans = list(ans)
space = []
space2 = []
cnt = 0

for i in ans:
    if i != " ":
        #space.append(i)
        if ord(i) < 97:
            space.append(ord(i) + 32)
        else:
            space.append(ord(i))

space = list(set(space))
space.sort()
ansList = []
for i in range(97, 123):
    ansList.append(i)

for i in range(len(ansList)):
    if ansList[i] not in space:
        cnt = 1
        space2.append(chr(ansList[i]))




if cnt == 1:
    print("YES")
    print("".join(space2))
else:
    print("NO")
#print(space)
#print(ansList)
