li = list(input())
n = int(input())
leftstack = [li[0]]
li = li[1:]
rightftstack = []
for i in reversed(range(len(li))):
    rightftstack.append(li[i])
#print(rightftstack)

for i in range(n):
    order = input()
    if order == "move right" and len(rightftstack) > 1:
        leftstack.append(rightftstack[-1])
        del rightftstack[-1]

    elif order == "move left" and len(leftstack) > 1:
        rightftstack.append(leftstack[-1])
        del leftstack[-1]

    elif order == "tear right" and len(rightftstack) > 1:
        del rightftstack[-1]

    elif order == "tear left" and len(leftstack) > 1:
        del leftstack[-1]

    #print(leftstack[-1], rightftstack[-1])

print(leftstack[-1], rightftstack[-1])