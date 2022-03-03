import sys
input = sys.stdin.readline

# 입력
N = int(input())
video = []
for _ in range(N):
    video.append(list(map(int, input().rstrip())))


# 분할정복(x, y, 입력크기)
def quadTree(x, y, n):
    for i in range(x, x + n):
        for j in range(y, y + n):
            # 같지 않으면 4분할
            if video[x][y] != video[i][j]:
                return '(' + quadTree(x, y, n // 2) + quadTree(x, y + n // 2, n // 2) + quadTree(x + n // 2, y, n // 2) + quadTree(x + n // 2, y + n // 2, n // 2) + ')'
    #모두 같으면 출력
    return str(video[x][y])

print(quadTree(0, 0, N))
