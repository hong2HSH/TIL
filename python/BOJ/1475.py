import math

N = input()
N = list(map(int, N))
dict = {}
for i in N:
    if i == 6:
        i = 9
    if i in dict:
        dict[i] += 1
    else:
        dict[i] = 1

dict[9] = math.ceil(max(dict.values()) / 2)

M = max(dict, key=dict.get)
if M == 9:
    print(max(dict.values()))
else:
    print(max(dict.values()))
