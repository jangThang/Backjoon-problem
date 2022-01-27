remainder = [0]*43
for i in range(10):
    n = int(input())
    n %= 42
    if remainder[n] == 0:
        remainder[n] += 1
print(sum(remainder))
