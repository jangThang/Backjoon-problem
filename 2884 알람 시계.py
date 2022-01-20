H, M = list(map(int, input().split()))
if M < 45:
    M += 15
    H -= 1
    if H < 0:
        H = 23

else:
    M -= 45
print (H, M)
