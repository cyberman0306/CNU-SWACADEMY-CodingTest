n = int(input())
li = list(map(int, input().split()))
ans = []
for i in range(len(li)):
    p = sum(li[0 : i+1])
    ans.append(p)
    for j in range(i):
        #print(j)
        #print(li[j])
        l = sum(li[0:j+1])
        #print('i is ',i, 'j is', j)
        #print('p is ',p, 'l is', l)
        #print(p-l)
        ans.append(p-l)
    #print()
print(max(ans))
#print(li)