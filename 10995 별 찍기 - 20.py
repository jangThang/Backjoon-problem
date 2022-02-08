N = int(input())

for i in range(N):
    #홀수행
    if i % 2 == 1:
       print(" ", end="")
    print("* "*(N-1) + "*")
