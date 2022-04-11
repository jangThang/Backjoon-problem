import sys
input = sys.stdin.readline

# 입력
A, B = input().rstrip().split()

# 브루트포스
if len(A) > len(B):  # 짧은 길이가 A
    A, B = B, A

# 두 문자열 차이 계산
def diff(a, b):
    n = len(a)
    res = 0
    for i in range(n):
        if a[i] != b[i]:
            res += 1
    return res

# A 길이만큼 B를 순회하며 판별
min_diff = 50
for i in range(len(B)-len(A)+1):
    min_diff = min(min_diff, diff(A, B[i:i+len(A)]))
print(min_diff)
