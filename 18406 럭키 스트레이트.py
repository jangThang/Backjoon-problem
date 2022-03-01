#입력
N = input()

pre = 0 #앞부분
for i in range(len(N)//2):
    pre += int(N[i])

post = 0 #뒷부분
for i in range(len(N)//2, len(N)):
    post += int(N[i])

if pre == post:
    print("LUCKY")
else:
    print("READY")
