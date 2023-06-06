T = int(input())

for _ in range(T):
    R, S = input().split()
    R = int(R)
    li = []
    for i in range(len(S)):
        for j in range(R):
            li.append(S[i])
    print("".join(li))
