import sys
input = sys.stdin.readline().rstrip

ans = input()
ans = list(ans)
space = []

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
if ansList == space:
    print("YES")
else:
    print("NO")
#print(space)
#print(ansList)
