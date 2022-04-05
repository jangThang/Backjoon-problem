import sys
input = sys.stdin.readline

# 입력
N = int(input())
rope = []
for _ in range(N):
    rope.append(int(input()))

# 내림차순 정렬
rope.sort(reverse=True)

# 그리디 알고리즘
res = 0
for idx, i in enumerate(rope, 1):
    res = max(res, idx*i)
print(res)
