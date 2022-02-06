T = int(input())
for i in range(T):
    x, s = input().split()
    res = list(s)
    res.pop(int(x)-1)
    print("".join(res))
