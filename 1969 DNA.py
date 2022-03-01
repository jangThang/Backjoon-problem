import sys
input = sys.stdin.readline

#입력
N, M = map(int, input().split())
dna = []
for _ in range(N):
    dna.append(input().rstrip())

res = ''
hammingDistSum = 0

#헤밍거리 계산
for i in range(M):
    hammingDist = {'A': 0, 'C': 0, 'G': 0, 'T': 0}
    for j in range(N):
        hammingDist[dna[j][i]] += 1
    res += max(hammingDist, key=hammingDist.get)
    hammingDistSum += (N - max(hammingDist.values()))
print(res)
print(hammingDistSum)
