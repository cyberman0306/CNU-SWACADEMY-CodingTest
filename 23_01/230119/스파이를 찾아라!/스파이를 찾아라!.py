import sys
input = sys.stdin.readline

n = int(input().strip())

for i in range(n):
    sequence = int(input())
    space = list(map(int, input().split()))
    #print(space)
    if space[0:3].count(space[0]) == 3: #최빈값 찾음
        stdNum = space[0]
    if space[0:3].count(space[0]) > 1: # 0번째 값이 최빈값일때
        stdNum = space[0]
    elif space[0:3].count(space[1]) > 1: # 1번째 값이 최빈값일때
        stdNum = space[1]
    elif space[0:3].count(space[2]) > 1: # 2번째 값이 최빈값일때
        stdNum = space[2]
    for j in range(len(space)):
        if space[j] != stdNum:
            print(j+1)
            break