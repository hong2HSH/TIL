N = int(input())

for _ in range(N):
    a = input()
    li = list(a)
    li1 = []
    for i in li:
        if i not in li1:
            li1.append(i)
        else:
            if li1[-1] != i:
                N -= 1
                break
print(N)
