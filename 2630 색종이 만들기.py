N = int(input())
colorPaper = []
for i in range(N):
    colorPaper.append(list(map(int, input().split())))
    
# 같은 색종이 판별기
# 모두 더했을 때 0 = 전부 0 / 모두 더했을때 N = 전부 1
def isSamePaper(x,y,n):
    _sum = 0
    for i in range(x, x+n):
        for j in range(y, y+n):
            _sum += colorPaper[i][j]
    if _sum == 0:
        return 0 # 하얀색
    elif _sum == n**2:
        return 1 # 파란색
    else:
        return -1 # 섞임
    
# 분할 정복
def searchPaper(a, b, n):
    x = isSamePaper(a,b,n)
    if x == -1: # 섞였을 경우, 4분할
        searchPaper(a, b, n//2)
        searchPaper(a + n//2, b, n//2)
        searchPaper(a, b + n//2, n//2)
        searchPaper(a + n//2, b + n//2, n//2)
    elif x == 0: # 모두 하얀색
        global white
        white += 1
        #print("white: ",white, f"({a},{b}), {n}")
        return
    elif x == 1: # 모두 파란색
        global blue
        blue += 1
        #print("blue: ",blue, f"({a},{b}), {n}")
        return

white = 0
blue = 0

searchPaper(0,0,N)
print(white)
print(blue)
