n, m = map(int, input().split())
li = []
for i in range(n):
    li.append([0] * n)

for i in range(m):
    a, b = map(int, input().split())
    li[a-1][b-1] = 1
    li[b-1][a-1] = 1

for i in range(len(li)):
    print(*li[i])
