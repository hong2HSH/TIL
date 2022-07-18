word = input()
a = 0
for i in word:
    if i in ['a','e','i','o','u']:
        a += 1
print(a)