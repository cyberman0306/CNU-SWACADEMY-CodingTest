t = int(input())

for _ in range(t):
    n, m = map(int, input().split())  # row , column
    space = []
    for i in range(n):
        getSpace = input()
        getSpace = list(getSpace)
        #print(getSpace)
        space.append(getSpace)
    #print(space)
    countControl = int(input())
    control = input()
    control = list(control)
    #print(countControl)
    #print(control)
    totalspace = []
    for j in range(len(space)):
        for p in range(len(space[j])):
            totalspace.append(space[j][p])
        #print(totalspace)
    #print()
    #print(totalspace.index("@"))
    junsikRow, junsikColumn = (totalspace.index("@") % m, totalspace.index("@") // m)
    print(totalspace.index("@") // m, totalspace.index("@") % m)
    #print(totalspace.index("@") % m)
    #print()

    for i in range(countControl):
        if control[i] == "L":
            junsikColumn -= 1
        elif control[i] == "R":
            junsikColumn += 1
        elif control[i] == "U":
            junsikRow -= 1
        elif control[i] == "D":
            junsikRow += 1


        if junsikColumn <= 0:
            junsikColumn = 0
            print("wall")
        if junsikColumn >= m:
            junsikColumn = m - 1
            print("wall")
        if junsikRow <= 0:
            print("wall")

            junsikRow = 0
        if junsikRow >= n:
            print("wall")

            junsikRow = n - 1
        print(junsikRow, junsikColumn)

    print("totoal", junsikRow, junsikColumn)
