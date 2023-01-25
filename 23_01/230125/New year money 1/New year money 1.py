n = int(input())

space = list(map(int, input().split()))

#print(space)

for i in range(n):
    count = 0
    for j in range(n):
        if space[j] > space[i]:
            count += 1
    if space.count(space[i]) == 1:
        print(n - count -1, count)
    else:
        print(n - count - space.count(space[i]), count)

