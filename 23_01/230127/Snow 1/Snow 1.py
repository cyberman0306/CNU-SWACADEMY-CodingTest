n = int(input())

r1, c1, r2, c2 = map(int, input().split())

space = []
space = [["*" for _ in range(n)] for _ in range(n)]

if r1 < r2:
    if c1 < c2:
        for i in range(r1-1, r2):
            for j in range(c1 - 1, c2):
                space[i][j] = "."
    else:
        for i in range(r1-1, r2):
            for j in range(c2 - 1, c1):
                space[i][j] = "."
else:
    if c1 < c2:
        for i in range(r2-1, r1):
            for j in range(c1 - 1, c2):
                space[i][j] = "."
    else:
        for i in range(r2-1, r1):
            for j in range(c2 - 1, c1):
                space[i][j] = "."


for i in space:
    print("".join(i))