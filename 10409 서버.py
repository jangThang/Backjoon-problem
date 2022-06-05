import sys
input = sys.stdin.readline

# 입력
n, T = map(int, input().split())
task = list(map(int, input().split()))

# 처리하는 일의 개수
cnt = 0
for i in task:
    if i <= T:
        T -= i
        cnt += 1
    else:
        break
print(cnt)
