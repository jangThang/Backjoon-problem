T = int(input())
for i in range(T):
    N = int(input())
    clothes = dict()
    for i in range(N):
        items, kinds = input().split()
        # 이미 있는 종류일 경우
        if kinds in clothes:
            clothes[kinds] += 1
        # 새로운 종류 추가
        else:
            clothes[kinds] = 1

    res = 1 # 결과값
    for i in clothes:
        res *= clothes[i]+1
    print(res-1)
