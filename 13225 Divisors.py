n = int(input())
for _ in range(n):
    c = int(input())
    res = 0
    for i in range(1, c+1):
        if c % i == 0:
            res += 1
    print(c, res)
