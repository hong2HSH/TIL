T = int(input())

for _ in range(T):
    a, b = map(int, input().split())
    sum = 0
    if a == 1:
        sum += 5000000
    elif 1 < a <= 3:
        sum += 3000000
    elif 3 < a <= 6:
        sum += 2000000
    elif 6 < a <= 10:
        sum += 500000
    elif 10 < a <= 15:
        sum += 300000
    elif 15 < a <= 21:
        sum += 100000
    else:
        sum += 0
    if b == 1:
        sum += 5120000
    elif 1 < b <= 3:
        sum += 2560000
    elif 3 < b <= 7:
        sum += 1280000
    elif 7 < b <= 15:
        sum += 640000
    elif 15 < b <= 31:
        sum += 320000
    else:
        sum += 0
    print(sum)
