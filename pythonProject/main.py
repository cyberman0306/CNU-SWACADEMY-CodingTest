n, k = map(int, input().split())
cnt = 0
newSpace = []
checkSpace = []
defaultSpace = ['a', 'n', 't', 'i', 'c']
alphabetList = list(set(chr(i) for i in range(97, 123)))
alphabetList.remove('a')
alphabetList.remove('n')
alphabetList.remove('t')
alphabetList.remove('i')
alphabetList.remove('c')
#print(alphabetList)
answerNums = n
for i in range(len(alphabetList)):
    checkSpace.append(0)

#print(checkSpace)
teachableLetterNums = k - 5
for i in range(n):
    if k < 5:
        cnt = 0
    else:
        newK = k - 5
        space = input()

        space = space.replace('a', '')
        space = space.replace('n', '')
        space = space.replace('t', '')
        space = space.replace('i', '')
        space = space.replace('c', '')

        newSpace = (sorted(space))
        #print(newSpace)
        #print(teachableLetterNums)
        for j in range(len(newSpace)):
            tempLetter = str(*newSpace[j])
            if teachableLetterNums < 1 and checkSpace[alphabetList.index(tempLetter)] == 0:
                answerNums -= 1
                break
            if teachableLetterNums > 0 and checkSpace[alphabetList.index(tempLetter)] == 0:
                checkSpace[alphabetList.index(tempLetter)] = 1
                teachableLetterNums -= 1

if k < 5:
    print(0)
elif k == 26:
    print(n)
else:
    print(answerNums)
