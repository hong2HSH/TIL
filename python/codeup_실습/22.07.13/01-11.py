a = range(2,10)
b = range(1,10)

for i in a:
    print(f'{i}단')
    for j in b:
        print(i,'X',j,'=', i*j)