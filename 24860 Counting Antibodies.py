# 입력
va, ja = map(int, input().split())
vb, jb = map(int, input().split())
vc, dc, jc = map(int, input().split())

# 계산
res = 0
heavy = vc*dc*jc
res += va*ja*heavy
res += vb*jb*heavy

# 출력
print(res)
