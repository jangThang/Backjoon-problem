# 입력
N = int(input())
board = [0]*N # 보드판
res = 0

# DFS 탐색
def dfs(x):
    global res # N개의 퀸을 놓는 경우의 수

    # 보드판 맨 끝에 도달해서 탐색마침(N개의 퀸 놓는 가짓수 +1)
    if x == N:
        res += 1
        return

    # 아직 탐색할 row가 남음
    else:
        # 해당 row의 1~N열 칸을 탐색
        for i in range(N):
            # x행, i열 탐색
            board[x] = i
            # 해당 칸이 다른 퀸이 겹치지 않는지 판별
            if isPromising(x):
                dfs(x+1)  # 겹치지 않으면 다음 행으로 이동
# 백트래킹
def isPromising(x):
    for i in range(x):
        # 다른 퀸과 열이 같거나, 대각선이면 False
        if board[x] == board[i] or abs(board[x] - board[i]) == x-i:
            return False
    return True

dfs(0)
print(res)
