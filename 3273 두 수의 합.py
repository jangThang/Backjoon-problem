import sys
input = sys.stdin.readline

# 입력
n = int(input())
numlist = list(map(int, input().split()))
x = int(input())

# 정렬
numlist.sort()

# x값 찾기
cnt = 0
start = 0
end = n-1

while start < end:
    num = numlist[start] + numlist[end]

    #x와 같은 경우
    if num == x:
        cnt += 1
        start += 1

    #x보다 작은 경우
    elif num < x:
        start += 1

    #x보다 큰 경우
    else:
        end -= 1

print(cnt)
