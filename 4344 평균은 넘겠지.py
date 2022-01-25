C = int(input())
for i in range(C):
    score = list(map(int, input().split()))
    N = score.pop(0)
    mean = sum(score)/N
    
    cnt = 0 # 평균 넘는 인원
    for j in score:
        if j > mean:
            cnt += 1
    res = (cnt/N) * 100
    print(f'{res:.3f}%')
