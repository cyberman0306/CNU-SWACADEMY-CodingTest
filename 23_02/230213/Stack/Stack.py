n = int(input())
li = []
for i in range(n):
    a = list(map(str, input().split()))
    if a[0] == 'push':
        #print(a)
        li.append(a[1])
    else:
        if len(li) == 0:
            print(-1)
        else:
            print(li[-1])
            li.pop(-1)
            #print(li)
#print(li)