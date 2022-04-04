from collections import Counter
import sys
input = sys.stdin.readline

# 입력
N = int(input())
numlist = []

for _ in range(N):
    numlist.append(int(input()))

# 개수 세기
counting = Counter(numlist).most_common()
max_freq = counting[0][1]  # 최빈값의 빈도
res = counting[0][0]  # 최빈값

for num, freq in counting:
    if freq == max_freq and num < res:
        res = num
print(res)
