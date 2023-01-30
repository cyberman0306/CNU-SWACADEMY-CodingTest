import sys
input = sys.stdin.readline

n = int(input())
space = [0] * 10001
for i in range(n):
    a = int(input())
    space[a] += 1

for i in range(10001):
    if space[i] != 0:
        for _ in range(space[i]):
            print(i)