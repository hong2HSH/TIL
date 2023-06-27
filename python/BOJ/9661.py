n = int(input())

li = ["SK", "CY", "SK", "SK", "CY"]

n = n % 5
if n == 0:
    n = 4
else:
    n -= 1
print(li[n])
