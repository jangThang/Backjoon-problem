import sys
input = sys.stdin.readline

#입력
N = int(input())
paper = []
for _ in range(N):
    paper.append(list(map(int, input().split())))

minus = 0 # -1인 종이
zero = 0 # 0인 종이
plus = 0 # 1인 종이

# 같은 종이 판별기
def isSamePaper(x, y, n):
    for i in range(x, x+n):
        for j in range(y, y+n):
           if paper[i][j] != paper[x][y]: #맨 처음 수와 다른 수가 나오면 섞인 것
                return False
    return True #모두 같은 숫자로 이루어짐

def searchPaper(a, b, n):
    if not isSamePaper(a, b, n): # 섞였을 경우, 9분할
        searchPaper(a, b, n//3) #(0,0)
        searchPaper(a + n//3, b, n//3) #(1,0)
        searchPaper(a + 2*(n//3), b, n//3) #(2,0)

        searchPaper(a, b+n//3, n//3) #(0,1)
        searchPaper(a, b+(n//3)*2, n//3) #(0,2)
        searchPaper(a+n//3, b+n//3, n//3) #(1,1)

        searchPaper(a+n//3, b+(n//3)*2, n//3) #(1,2)
        searchPaper(a+(n//3)*2, b+n//3, n//3) #(2,1)
        searchPaper(a+(n//3)*2, b+(n//3)*2, n//3) #(2,2)

    else:
        if paper[a][b] == -1: #모두 -1
            global minus
            minus += 1
            # print("minus: ",minus, f"({a},{b}), {n}")
            return
        elif paper[a][b] == 0: #모두 0
            global zero
            zero += 1
            # print("zero: ",zero, f"({a},{b}), {n}")
            return
        else: #모두 1
            global plus
            plus += 1
            # print("plus: ",plus, f"({a},{b}), {n}")
            return

searchPaper(0, 0, N)
print(minus)
print(zero)
print(plus)
