import sys
input = sys.stdin.readline

# 입력
left_stack = list(input().rstrip())
right_stack = []

M = int(input())
for _ in range(M):
    command = input().rstrip()
    if command == 'L':
        # 왼쪽 스택이 비어있지 않다면, 1글자를 오른쪽 스택으로 옮김
        if left_stack:
            right_stack.append(left_stack.pop())

    elif command == 'D':
        # 오른쪽 스택이 비어있지 않다면, 1글자를 왼쪽 스택으로 옮김
        if right_stack:
            left_stack.append(right_stack.pop())

    elif command == 'B':
        # 왼쪽 스택 1글자 삭제
        if left_stack:
            left_stack.pop()

    else:
        # 왼쪽 스택 1글자 추가
        left_stack.append(command[-1])

# 문자열 합친 후 출력
left_stack.extend(reversed(right_stack))
print(''.join(left_stack))
