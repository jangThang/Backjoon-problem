N = int(input())
for i in range(N):
    k = input()
    if int(k[-1])%2 == 1:
        print('odd')
    else:
        print('even')
