import sys
input = sys.stdin.readline

#입력
n = int(input()) #테스크케이스
for _ in range(n):
    p = int(input()) #선수 수
    player = dict()
    for i in range(p):
        cost, name = input().rstrip().split()
        player[name] = int(cost)
    print(max(player, key=player.get))
