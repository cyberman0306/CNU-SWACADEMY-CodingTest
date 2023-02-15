a, b = map(int, input().split())
#print(a, b)
if a > b:
    cnt = 0
    while a > b:
        if a - b == 1:
            print(a - b, cnt)
            break
        a -= 1
        b += 1
        cnt += 1
    if a - b != 1:
        print(b - a, cnt)
elif a < b:
    cnt = 0
    while a < b:
        if b - a == 1:
            print(b - a, cnt)
            break
        else:
            a += 1
            b -= 1
            cnt += 1
            #print(a, b, cnt)
    if b - a != 1:
        print(a - b, cnt)
else:
    print(0, 0)