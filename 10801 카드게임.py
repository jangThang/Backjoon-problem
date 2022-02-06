A = list(map(int, input().split()))
B = list(map(int, input().split()))

scoreA = 0
scoreB = 0
for i in range(10):
    if A[i] > B[i]:
        scoreA += 1
    elif A[i] < B[i]:
        scoreB += 1
if scoreA > scoreB:
    print("A")
elif scoreA < scoreB:
    print("B")
else:
    print("D")
