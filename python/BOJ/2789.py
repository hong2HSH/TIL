li = ['C','A','M','B','R','I','D','G','E']
a = list(map(str,input()))
ans = []
for i in a:
    if i not in li:
        ans.append(i)
print(''.join(ans))