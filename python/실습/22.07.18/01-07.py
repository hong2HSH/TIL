number_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

total = 0
count = 0

for number in number_list:
    total += number
# count가 for문 밖에 있어서 1로 출력된다 for 문 안쪽으로 넣어줌
    count += 1

# "//"는 몫이므로 "/"를 써준다
print(total / count)
