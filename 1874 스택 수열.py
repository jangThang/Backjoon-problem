import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
stack = deque([1]) #스택
operation = ['+'] #스택연산
cnt = 1 #최대 n까지
impossible = False

for i in range(n):
     x = int(input())

     # x가 클 경우 더하기
     while cnt < x:
         cnt += 1
         stack.append(cnt)
         operation.append('+')

     # 맨 위에 x가 있을 시 꺼내기
     if len(stack) != 0 and stack[-1] == x:
         stack.pop()
         operation.append('-')

     # 그 외에는 안되는 수열
     else:
         impossible = True

if impossible:
    print("NO")
else:
    print("\n".join(operation))
