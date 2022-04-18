from itertools import combinations
import sys
input = sys.stdin.readline

while True:
    # 입력
    numlist = list(map(int, input().split()))
    if numlist == [0]:
        break

    # 조합 구하기
    lotto = combinations(numlist[1:], 6)

    # 출력
    for i in lotto:
        for j in i:
            print(j, end=" ")
        print()
    print()
