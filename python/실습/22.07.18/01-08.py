word = "HappyHacking"

count = 0

for char in word:
    # 원래는 char 값이 a냐 e냐 i냐...를 보는 것이 아니었고 타입을 봤기때문에 전부 True로 인식했음
    # 각각 따로 타입을 지정해주면 그 값이 a냐 e냐 i냐...로 볼 수 있음
    if char == "a" or char ==  "e" or char ==  "i" or char == "o" or char ==  "u":
        count += 1

print(count)