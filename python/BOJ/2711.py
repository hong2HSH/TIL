T = int(input())

for i in range(T):
    a, b = map(str,input().split())
    a = int(a)
    b = list(b)
    b.pop(a-1)
    print(''.join(b))