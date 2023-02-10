n, m = map(int,input().split())
li = list(input())
#print(li)

for i in range(m):
    cnt = 0
    L, R = map(int,input().split())
    for j in range(L-1, R):
        if li[j] == 'e':
            cnt += 1
    print(cnt)