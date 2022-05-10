import sys
input = sys.stdin.readline

# 입력
board = input().rstrip() + '.'

# 덮어쓰기
new_board = ''
x_cnt = 0
for s in board:
    # X이면 카운트 +1
    if s == 'X':
        x_cnt += 1

    # .이면 정산 후 반영
    else:
        if x_cnt % 2 == 1:
            print(-1)
            break

        new_board += 'AAAA' * (x_cnt//4)
        x_cnt %= 4

        new_board += 'BB' * (x_cnt//2)
        x_cnt = 0
        new_board += '.'

else:
    print(new_board[:-1])
