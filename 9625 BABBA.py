K = int(input())
a = 1 #맨 처음 A 하나
b = 0
for i in range(K):
    preA = a
    # B -> BA
    a += b
    # A -> B
    a -= preA
    b += preA
print(a, b)
