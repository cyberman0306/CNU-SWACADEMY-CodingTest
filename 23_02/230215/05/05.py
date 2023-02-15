import sys

ans = sys.stdin.readline().rstrip()
ans = list(ans)
ansSumString = ""

q = int(sys.stdin.readline().rstrip())
for p in range(q):
    ansList = []
    for i in range(97, 123):
        ansList.append(i)
    space = []
    a, b = map(int, sys.stdin.readline().rstrip().split())
    for i in ans[a-1:b]:
        if i != " ":
            if ord(i) < 97:
                if (ord(i) + 32) in ansList:
                    ansList.remove(ord(i) + 32)
            else:
                if ord(i) in ansList:
                    ansList.remove(ord(i))
        if len(ansList) == 0:
            ansSumString += "1"
            break
    if len(ansList) != 0:
        ansSumString += "0"
print(ansSumString)