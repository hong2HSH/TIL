T = int(input())
for i in range(T) :
    s = input().strip()
    print(f'#{i+1}{int(s==s[::-1])}' )