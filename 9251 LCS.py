import sys
input = sys.stdin.readline

# 입력
a = input().rstrip()
b = input().rstrip()

# DP
len_a, len_b = len(a), len(b)
cache = [0] * len_b
for i in range(len_a):
    cnt = 0
    for j in range(len_b):
        # 최대 누적값 유지
        if cnt < cache[j]:
            cnt = cache[j]
        # 철자가 같으면 cnt + 1
        elif a[i] == b[j]:
            cache[j] = cnt + 1
print(max(cache))
