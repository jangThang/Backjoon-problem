import sys
input = sys.stdin.readline

n = int(input())
S = [0]*21 # x는 1부터 20
for i in range(n):
    operation = input().rstrip()
    if operation == 'all': #1로 초기화
        S = [1]*21
    elif operation == 'empty': #0으로 초기화
        S = [0]*21
    else:
        op, x = operation.split()
        if op == 'add':
            S[int(x)] = 1 #추가
        elif op == 'remove':
            S[int(x)] = 0 #제거
        elif op == 'check':
            print(S[int(x)]) #확인
        elif op == 'toggle':
            if S[int(x)] == 0:
                S[int(x)] = 1 #0이면 1
            else:
                S[int(x)] = 0 #1이면 0
