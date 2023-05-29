import sys


while 1:
    a = input()
    li = []
    cnt = 0
    if a == ".":
        break

    for i in a:
        if i == "[" or i == "(":
            li.append(i)
        elif i == "]":
            if li and li[-1] == "[":
                li.pop()
            else:
                cnt += 1
                break
        elif i == ")":
            if li and li[-1] == "(":
                li.pop()
            else:
                cnt += 1
                break

    if cnt == 0:
        if not li:
            print("yes")
        else:
            print("no")
    else:
        print("no")
