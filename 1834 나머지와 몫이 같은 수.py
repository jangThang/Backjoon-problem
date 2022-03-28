# 입력
N = int(input())

# N까지 나머지와 몫이 같은 수 합하기
res = 0
for i in range(N):
    res += N*i + i  # 나머지와 몫이 같은 수
print(res)
