n = int(input())

li = list(map(int, input().split()))
#print(li)
answerLi = []
sum = 0

for i in range(len(li)):
    sum += li[i]
    answerLi.append(sum)

print(*answerLi)
