L, R = map(int, input().split())

if L == R:
    a = list(str(L))
    print(a.count("8"))
else:
    a = R - L  ## 큰 값에서 작은 값을 뺀 값이 a
    b = 10 ** len(str(a))
    ans_L = list(str(L // b))
    cnt_L = ans_L.count("8")
    ans_R = list(str(R // b))
    cnt_R = ans_R.count("8")
    print(min(cnt_L, cnt_R))
