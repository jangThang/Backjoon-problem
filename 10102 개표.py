V = int(input())
vote = input()

A = 0
B = 0
for v in vote:
    if v == 'A':
        A += 1
    else:
        B += 1

#출력
if A > B:
    print("A")
elif A < B:
    print("B")
else:
    print("Tie")
