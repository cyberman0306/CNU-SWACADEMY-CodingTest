import sys
input = sys.stdin.readline
n = int(input())

for i in range(n):
    length, count = map(int, input().split())
    space = input()
    answer = 0
    memo = []
    for j in range(count):
        a, b = map(int, input().split())
        if memo.count((a, b)):
            answer += 1
        else:
            if len(space) >= 3:
                if space[a-1] == "U":
                    if b - a >= 2:
                        if space.count("m", a - 1, b) == b - a:
                            answer += 1
                            memo.append((a, b))
    print(answer)