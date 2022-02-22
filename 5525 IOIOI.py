import sys
input = sys.stdin.readline

N = int(input()) #Pn
Pn = 'I'+"OI"*N

M = int(input()) #S의 길이
S = input().rstrip()

res = 0
i = 0
while i < M-len(Pn):
    #Pn이 있으면 1 카운트하고, 2칸 앞으로 이동
    if S[i:i+len(Pn)] == Pn:
        res += 1
        i += 1
    i += 1
print(res)
