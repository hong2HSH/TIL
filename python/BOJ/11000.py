import sys
input = sys.stdin.readline

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]

li.sort(key=lambda x : (x[0],x[1]))
cnt = 0
while 1:
    num = 0
    li1 = []
    if len(li)<1:
        break
    for i in range(len(li)):
        if li[i][0] >= num:
            num = li[i][1]
        else :
            li1.append(li[i])
    cnt += 1
    li = li1
print(cnt)