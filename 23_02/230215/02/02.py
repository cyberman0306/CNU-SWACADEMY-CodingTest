n, m = map(int, input().split())
#print(n, m)
li = []
for i in range(n):
    li.append(i+1)
#print(li)
for i in range(m):
    a, b = map(int, input().split())
    tempA = li[a-1]
    #print(tempA)
    tempB = li[b-1]
    #print(tempB)
    li[a-1] = tempB
    li[b-1] = tempA
    #print(li)
print(*li)