space = []
count = 0
a = ""
a = input()
for i in range(len(a)):
    space.append(int(a[i]))
#print(space)

for i in range(len(space)):
    if space[i] == 1:
        count += 1

if count == 0:
    print(5)
else:
    print(count)