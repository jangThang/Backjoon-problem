# 기차의 속도, 파리의 속도, 두 기차의 거리
S, T, D = map(int, input().split())
print(T*(D//(2*S))) #D는 2*S의 배수
