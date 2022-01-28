def selfNumber(n):
    res = n
    #각 자릿수 더하기
    while n != 0:
        res += n%10
        n //= 10
    return res

number = [0]*10001
for i in range(10001):
    # 생성자 계산
    d = selfNumber(i)
    if d < 10001:
        number[d] += 1
        
    # 셀프넘버 출력
    if number[i] == 0:
        print(i)
