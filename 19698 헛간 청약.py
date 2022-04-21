# 입력
N, W, H, L = map(int, input().split())

# 헛간에 들어갈 수 있는 소의 개수
cow = (W//L) * (H//L)

# 출력
print(min(N, cow))
