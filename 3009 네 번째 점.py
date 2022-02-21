a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

if a == c:
    g = e
elif c == e:
    g = a
else:
    g = c

if b == d:
    h = f
elif d == f:
    h = b
else:
    h = d

print(g, h)
