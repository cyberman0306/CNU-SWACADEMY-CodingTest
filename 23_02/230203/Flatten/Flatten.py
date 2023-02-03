n = int(input())

li = list(map(int, input().split()))
#print(li)

stdNum = -1
cnt = 0
stdLow = min(li)
for i in range(len(li)):
    if li[i] > stdLow:
        cnt += (li[i] - stdLow)
        #print(cnt)

print(cnt)