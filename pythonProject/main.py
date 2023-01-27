n = int(input())
space = [[0 for _ in range(101)] for _ in range(101)]
#print(space)

for _ in range(n):
    start, end = map(int, input().split())

    for i in range(start, start + 10):
        for j in range(end, end + 10):
            space[i][j] = 1

count = 0
for row in space:
    count += row.count(1)
print(count)