man = 0
manMax = 0
for i in range(10):
    minus, plus = map(int, input().split())
    man -= minus
    man += plus
    if manMax < man:
        manMax = man
print(manMax)
