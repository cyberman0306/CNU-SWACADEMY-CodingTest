import sys
n = int(sys.stdin.readline())
li = []
for i in range(n):
    x, y = map(int, input().split())
    li.append([y, x])

li = sorted(li)
#print(*li)
for i in range(len(li)):
    print(li[i][1], li[i][0])