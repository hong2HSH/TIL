string = input()
dic = {}
for i in string:
    if i in dic:
        dic[i] += 1
    else :
        dic[i]= 1
for i in dic:
    print(i,dic[i])