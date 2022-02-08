N = int(input())

divided = 2 #나누는 수
while N != 1: #약수로 나눠서 1이 될 때까지 반복
    if N % divided == 0: #나누어질 경우
        print(divided) #약수 출력
        N //= divided #약수로 나누기
        divided = 1 #나누는 수 초기화
    divided += 1
