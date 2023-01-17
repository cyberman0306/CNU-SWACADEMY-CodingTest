t = int(input())

for _ in range(t):
    n, m = map(int, input().split())  # row , column
    space = []
    for i in range(n):
        getSpace = input()
        getSpace = list(getSpace)
        space.append(getSpace)
    countControl = int(input())
    control = input()
    control = list(control)
    totalspace = []
    for j in range(len(space)):
        for p in range(len(space[j])):
            totalspace.append(space[j][p])

    junsikRow, junsikColumn = (totalspace.index("@") // m + 1, totalspace.index("@") % m + 1)
    junsikhurt = 0
    for i in range(countControl):
        if control[i] == "L":
            junsikColumn -= 1
        elif control[i] == "R":
            junsikColumn += 1
        elif control[i] == "U":
            junsikRow -= 1
        elif control[i] == "D":
            junsikRow += 1

        if junsikColumn < 1:
            junsikColumn = 1
        if junsikColumn > m:
            junsikColumn = m
        if junsikRow < 1:
            junsikRow = 1
        if junsikRow > n:
            junsikRow = n
        if space[junsikRow-1][junsikColumn-1] == "#":
            if control[i] == "L":
                junsikColumn += 1
            elif control[i] == "R":
                junsikColumn -= 1
            elif control[i] == "U":
                junsikRow += 1
            elif control[i] == "D":
                junsikRow -= 1
        if space[junsikRow - 1][junsikColumn - 1] == "^":
            junsikhurt += 1

    print(junsikRow, junsikColumn, junsikhurt)
