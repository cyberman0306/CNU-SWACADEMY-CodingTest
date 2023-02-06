n, m = map(int, input().split())

li = list(map(int, input().split()))
total = 0
#print(li)

for i in range(m):
    total = 0
    L, R = map(int, input().split())
    for j in range(L-1, R):
        total += li[j]
    print(total)



#print(total)