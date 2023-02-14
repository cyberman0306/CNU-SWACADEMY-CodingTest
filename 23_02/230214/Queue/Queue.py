n = int(input())
li = []
for i in range(n):
    a = list(map(str, input().split()))
    if a[0] == 'push':
        #print(a)
        li.append(a[1])
    else: #pop일때
        if len(li) == 0: #스택에 없으면
            print(-1)
        else:
            print(li[0]) # 선입선출
            li.pop(0) # 마지막 원소를 출력, 제거
            #print(li)
#print(li)