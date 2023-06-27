n = int(input())
cnt = False
a = n % 7
if a == 1:
    cnt = True
elif a == 3:
    cnt = True
if cnt == True:
    print("CY")
else:
    print("SK")
