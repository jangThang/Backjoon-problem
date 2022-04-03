import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    A, B, C, D, E = map(int, input().split())
    print(f'${(A*350.34 + B*230.9 + C*190.55 + D*125.3 + E*180.9):.2f}')
