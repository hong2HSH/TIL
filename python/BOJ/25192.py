N = int(input())
cnt = 0
li = set()

for _ in range(N):
    a = input()
    if a != "ENTER":
        if a not in li:
            cnt += 1
            li.add(a)
    elif a == "ENTER":
        li = set()

print(cnt)
