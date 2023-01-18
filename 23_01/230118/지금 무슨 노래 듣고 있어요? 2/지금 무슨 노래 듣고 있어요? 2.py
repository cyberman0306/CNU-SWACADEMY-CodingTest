import sys
input = sys.stdin.readline

n = int(input())

nameList = []
songLength = []
songLengthSum = []
timeNow = 0

for _ in range(n):
    #a = sys.stdin.readline().strip()
    a = input().strip()
    nameList.append(a) #이름 공간

for i in range(n):
    a = int(sys.stdin.readline().strip())
    #곡하나의 길이 리스트
    songLength.append(a)
    #곡 누적길이의 리스트
    if i == 0:
        songLengthSum.append(a)
    else:
        songLengthSum.append(songLengthSum[i-1] + a)

#print(songLengthSum)
#print(nameList)
#print(songLength)
m = int(input())

for i in range(m):
    timeNow = int(input().strip())
    #print(timeNow)

    for j in range(len(songLengthSum)):
        while True:
            #나누기
            if timeNow > songLengthSum[-1]:
                timeNow -= songLengthSum[-1]
            else:
                break
        if timeNow <= songLengthSum[j]:
            #print(timeNow)
            print(nameList[j])
            break
