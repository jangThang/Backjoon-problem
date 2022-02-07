N = int(input())
num = 666 #악마의 숫자 666부터 시작
cnt = 0

while True:
    if "666" in str(num): #666이 있는지 확인
        cnt += 1
    if cnt == N:
        print(num)
        break
    num += 1
