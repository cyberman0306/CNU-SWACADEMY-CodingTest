def seller(space, incomeTarget, buyingDate):
    space2 = []
    for i in space[int(buyingDate) - 1: ]:
        space2.append(i)
    incomeTarget = int(space[int(buyingDate)-1]) + incomeTarget
    for j in range(len(space2)):
        if int(space2[j]) >= incomeTarget:
            answer = j + buyingDate
            break
        else:
            answer = "JB"
    return answer

n = int(input())

for i in range(n):
    n, incomeTarget, buyingDate = map(int, input().split())
    space = []
    space = input().split()
    space = list(space)
    #print(space)
    print(seller(space, incomeTarget, buyingDate))
