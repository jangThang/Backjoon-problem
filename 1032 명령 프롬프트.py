import sys
input = sys.stdin.readline

#입력
string = []
T = int(input())
for _ in range(T):
    string.append(input().rstrip())

#비교
n = len(string[0]) #문자열 길이
for i in range(n):
    same = True
    for j in range(1, T):
        #다른 문자열이 있으면 False
        if string[0][i] != string[j][i]:
            same = False
    print(string[0][i] if same else '?', end='')
