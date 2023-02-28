n, m = map(int, input().split())
ans = True
li = [[0] * n for _ in range(n)]
# for i in range(len(li)):
#     print(li[i])

for i in range(m):
    a, b = map(int, input().split())
    li[a-1][b-1] += 1
    li[b-1][a-1] += 1

for i in range(len(li)):
    if 2 in li[i]:
        ans = False

if ans is True:
    print("YES")
else:
    print("NO")