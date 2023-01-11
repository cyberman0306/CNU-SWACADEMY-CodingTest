def seller(space, incomeTarget, buyingDate):
    space2 = []
    for i in space[int(buyingDate) - 1: ]:
        space2.append(i)
    #print(space2)
    incomeTarget = int(space[int(buyingDate)-1]) + incomeTarget
    #print(incomeTarget)
    #print(space2.index(str(incomeTarget)))
    if str(incomeTarget) in space2:
        answer = space2.index(str(incomeTarget))
        answer += buyingDate
        return answer
    else:
        return "JB"


n = int(input())



for i in range(n):
    n, incomeTarget, buyingDate = map(int, input().split())
    space = []
    space = input().split()
    space = list(space)
    #print(space)
    print(seller(space, incomeTarget, buyingDate))

# 목표값 이상이기만 하면됨