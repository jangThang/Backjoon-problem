N, r, c = map(int, input().split()) #2^N * 2^N 중 r행 c열

num = 0
#분할 정복
while N != 0:
    N -= 1
    # 1사분면
    if r < 2**N and c < 2**N:
        num += 0

    # 2사분면
    elif r < 2**N and c >= 2**N:
        num += (2**N) * (2**N)*1
        c -= 2**N

    # 3사분면
    elif r >= 2**N and c < 2**N:
        num += (2**N) * (2**N)*2
        r -= 2**N

    # 4사분면
    else:
        num += (2**N) * (2**N)*3
        r -= 2**N
        c -= 2**N
print(num)
