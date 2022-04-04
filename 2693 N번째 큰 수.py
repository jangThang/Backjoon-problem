import sys
input = sys.stdin.readline

# 입력
T = int(input())
for _ in range(T):
    numlist = list(map(int, input().split()))

    # 정렬
    numlist.sort()

    # 세 번째로 큰 값 출력
    print(numlist[7])
