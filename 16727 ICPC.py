# 입력
p1, s1 = map(int, input().split())
s2, p2 = map(int, input().split())

# 출력
if p1+p2 > s1+s2:
    print("Persepolis")
elif p1+p2 < s1+s2:
    print("Esteghlal")
else:  # 동점인 경우
    if s1 > p2:
        print("Esteghlal")
    elif s1 < p2:
        print("Persepolis")
    else:
        print("Penalty")
