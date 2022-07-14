word = input()
word = list(word)
a = 0
for i in word:
    a = ord(i)
    print(chr(a-32),end='')