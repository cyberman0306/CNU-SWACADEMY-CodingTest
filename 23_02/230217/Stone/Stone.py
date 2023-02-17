n, m = map(int, input().split())
tower = []
for i in range(n):
    tower.append(i+1)
for i in range(m):
    li = input()
    if li == 'raise':
        a = tower.pop(0)
        #del tower[0]
        tower.append(a)
    elif li == 'discard':
        if len(tower)>1:
            del tower[0]
    #print(tower)

print(tower[0])