n = int(input())
space = []
for i in range(n):
    space.append(int(input()))

#print(space)
space.sort()
count = 0
space2 = list(set(space))

for i in space:
    count += i

for i in space2:

print(round(count//n), 1)
print(space[n//2])

print(max(space) - min(space))