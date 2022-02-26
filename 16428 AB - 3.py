A, B = map(int, input().split())
if B > 0:
    print(A//B)
    print(A%B)
#B가 음수일 때
else:
    print(-(A//-B))
    print(A%-B)
