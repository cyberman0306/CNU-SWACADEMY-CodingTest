n = int(input())
liB = list(map(int, input().split()))
m = int(input())
liQ = list(map(int, input().split()))

sumli = []
sumit = 0
ans = 0
for i in range(len(liB)):
    sumit += liB[i]
    sumli.append(sumit)

for i in range(m):
    for j in range(len(sumli)):
        if liQ[i] <= sumli[j]:
            ans += j+1
            break
        if liQ[i] > sumli[-1]:
            ans += n
            break

print(ans % 1000000007)