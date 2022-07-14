word = input()
a = 0
for i in range(len(word)):
    if word[i] == 'a':
        print(i)
        a += 1
        break
if a == 0:
    print(-1)