n = int(input())

for i in range(n):
    a, b = map(int, input().strip().split(' '))
    answer = 0
    for i in range(max(a, b), (a * b) + 1):
        if i % a == 0 and i % b == 0:
            answer = i
            break
    if answer == (a * b):
        print("Perfect")
    else:
        print("Not even close")



