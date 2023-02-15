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
#print(sumli)
for i in range(m):
    for j in range(len(sumli)):
        #print(liQ[i], sumli[j])
        if liQ[i] <= sumli[j]:
            #print(j+1)
            ans += j+1
            #print()
            break

#print()
#print(ans)
print(ans % 1000000007)