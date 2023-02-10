n = int(input())
li = list(input())
value = []
for i in range(n):
    a = li[ : i]
    #print(a)
    aSort = set(a)
    #print(aSort)
    b = li[i:]
    #print(b)
    bSort = set(b)
    #print(bSort)
    value.append((len(a) - len(aSort)) + (len(b) - len(bSort)))
    #print()
#print(value)

print(n - min(value))