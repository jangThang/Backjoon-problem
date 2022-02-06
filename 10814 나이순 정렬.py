import sys
input = sys.stdin.readline

N = int(input())
member = []
for i in range(N):
    age, name = input().split()
    member.append([int(age), name])

member.sort(key=lambda x: x[0]) # 나이순대로 정렬

for age, name in member:
    print(age, name)
