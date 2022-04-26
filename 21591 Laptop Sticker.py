# 입력
# 노트북 너비, 높이 / 스티커 너비, 높이
wc, hc, ws, hs = map(int, input().split())

# 판별
if wc >= ws + 2 and hc >= hs + 2:
    print(1)
else:
    print(0)
