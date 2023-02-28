n, m = map(int, input().split())
li = [[] for i in range(n)]
#print(li)

for i in range(m):
    a, b = map(int, input().split())
    li[a-1].append(b)
    li[b-1].append(a)
for i in range(len(li)):
    z = li[i]
    z.sort()
    if len(z) == 0:
        print(-1)
    else:
        print(*z)