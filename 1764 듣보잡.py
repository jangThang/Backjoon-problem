import sys
input = sys.stdin.readline

N, M = map(int, input().split())
noHear = set() #듣도 못한 사람
noSee = set() #듣보잡
for _ in range(N):
    noHear.add(input().rstrip())
for _ in range(M):
    noSee.add(input().rstrip()) #보도 못한 사람

noHearSee = sorted(list(noHear & noSee)) #교집합 중 사전순 정렬

print(len(noHearSee))
for name in noHearSee:
    print(name)
