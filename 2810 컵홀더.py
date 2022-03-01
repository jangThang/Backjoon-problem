#입력
N = int(input())
seat = input()

cupholder = 1 #컵홀더의 개수 (맨 왼쪽 컵홀더)
for s in seat:
    if s == 'S':
        cupholder += 1
    elif s == 'L':
        cupholder += 0.5

#출력
print(min(N, int(cupholder)))
