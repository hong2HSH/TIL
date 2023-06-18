N = int(input())
li = []
dict = {}
num = []

for _ in range(N):
    li.append(input().split())

for i in range(n):
    for j in range(len(li[i])):
        if li[i][j] in dict:
            dict[li[i][j]] += 10 ** (len(li[i]) - j - 1)
        else:
            dict[li[i][j]] = 10 ** (len(li[i]) - j - 1)

for k in dict.values():
    num.append(k)

num.sort(reverse=True)

sum = 0
a = 9
for l in num:
    sum += a * l
    a -= 1
print(sum)
