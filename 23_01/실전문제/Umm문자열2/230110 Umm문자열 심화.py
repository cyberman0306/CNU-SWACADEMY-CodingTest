
def checker(space, answer):
    if len(space) >= 3:
        if space.count("U") == 1:
            if space[0] == "U":
                answer += 1
                return answer
            else:
                checker(space[1:], answer)
    return answer

def checker2(space, answer):
    if space[0] == "U":
        if len(space) >= 3:
            if space.count("U") == 1:
                answer += 1
                return answer
    else:
        if "U" in space:
            U = space.index("U")
            checker2(space[U:], answer)
    return answer

n = int(input())
for i in range(n):
    length, count = map(int, input().split())
    space = input()
    space = list(space)
    answer = 0
    for j in range(count):
        space2 = []
        a, b = map(int, input().split())
        answer = checker2(space[a - 1:b], answer)
    print(answer)