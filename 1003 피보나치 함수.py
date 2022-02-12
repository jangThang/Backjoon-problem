import sys
input = sys.stdin.readline

fibo = [[-1] * 2] * 41 # [-1, -1]로 초기화 (최대 N은 40)
fibo[0] = [1, 0] #0의 갯수 / 1의 갯수
fibo[1] = [0, 1]

for i in range(2, 41):
    fibo[i] = [fibo[i-1][0] + fibo[i-2][0], fibo[i-1][1] + fibo[i-2][1]]

T = int(input())
for i in range(T):
    n = int(input())
    print(fibo[n][0], fibo[n][1])
