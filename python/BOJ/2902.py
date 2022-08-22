a = list(map(str,input()))
print(a)
list = []
for i in range(len(a)):
    if a[i] == '-':
        list.append(a[i+1])
print(a[0],*list, sep='')