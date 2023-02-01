n = int(input())
space = list(map(int, input().split()))
a = 0
gap = -1
ans = 0
z = 0

for i in space:
    if i == 320:
        print((space.index(i)+1))
        z = 1
        break

    if 320 - int(i) < 0:
        a = -1 * (320 - int(i))
    else:
        a = 320 - int(i)

    if gap == -1:
        gap = a
        ans = (space.index(i)+1)
    else:
        if a < gap:
            ans = (space.index(i)+1)
            gap = a

if z != 1:
    print(ans)