import sys
input = sys.stdin.readline

# 하노이의 탑 알고리즘
def hanoi_tower(n, start, end):
    # n이 1이 되면 종료
    if n == 1:
        print(start, end)
        return

    # 1단계, n-1개의 원판을 시작 막대에서 보조 막대로 옮김
    hanoi_tower(n-1, start, 6-start-end)
    
    # 2단계, 맨 아랫 원판을 시작 막대에서 목표 막대로 옮김
    print(start, end)
    
    # 다시 1, 2단계를 반복하기 위한 재귀호출
    hanoi_tower(n-1, 6-start-end, end)

# 입력
n = int(input())
print(2**n-1)  # 옮긴 횟수 K
hanoi_tower(n, 1, 3)
