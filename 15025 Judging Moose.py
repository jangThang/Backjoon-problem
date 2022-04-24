# 입력
l, r = map(int, input().split())

# 출력
if l == r == 0:
    print("Not a moose")
elif l == r:
    print("Even", l+r)
else:
    print("Odd", max(l, r)*2)
