n = int(input())
li = list(map(int, input().split()))
z = 0
for i in range(n):
    #print(sum(li[0:i]))
    #print(sum(li[i+1:n]))
    if n == 1:
        z = 1
        print(1)
        break
    elif i != n and sum(li[0:i]) == sum(li[i+1:n]):
        print(i+1)
        z = 1
        break
if z != 1:
    print(-1)
    # else:
    #     print(-1)
    #     break