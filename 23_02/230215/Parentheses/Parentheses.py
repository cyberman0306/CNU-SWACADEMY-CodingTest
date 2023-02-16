li = list(input())
ans = "NO"
if li.count('(') != li.count(')'):
    ans = "NO"
else:
    for i in range(li.count('(')):
        if li.index("(") < li.index(")"):
            li.remove("(")
            li.remove(")")
    if len(li) == 0:
        ans = "YES"
print(ans)
