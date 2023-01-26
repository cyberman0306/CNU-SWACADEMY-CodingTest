n = int(input())
space = list(map(int, input().split()))

a = 0
a2 = 0
count = 0
count2 = 0
for i in space:
    if a < i:
        a = i
        count += 1

for i in reversed(space):
    #print(i)
    if a2 < i:
        a2 = i
        count2 += 1

print(count, count2)