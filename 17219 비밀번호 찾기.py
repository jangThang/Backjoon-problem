import sys
input = sys.stdin.readline

N, M = map(int, input().split())
memo = dict() #사이트 주소 - 비밀번호 쌍을 기억할 딕셔너리
for _ in range(N):
    site, password = input().rstrip().split()
    memo[site] = password

for _ in range(M):
    site = input().rstrip()
    print(memo[site])
