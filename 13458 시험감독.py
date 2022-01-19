N = int(input())
A = list(map(int,input().split()))
B, C = map(int, input().split())

master = N
sub = 0
for i in A:
    if i-B > 0:
        sub += (i-B)//C
        if (i-B) % C != 0:
            sub += 1
print(master+sub)
