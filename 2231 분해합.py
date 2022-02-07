N = int(input())
res = 0 #결과값
for i in range(1, N):
    subSum = 0 #분해합
    num = i
    #각 자릿수 더하기
    while num != 0:
        subSum += (num % 10)
        num //= 10
        
    #자기 자신과 각 자릿수 합이 N과 같아야 생성자
    if subSum+i == N:
        res = i
        break
print(res)
