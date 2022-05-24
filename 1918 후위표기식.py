# 입력
s = input()

# 스택을 이용한 후위표기식
stack = []
res = ''
for i in s:
    # 피연산자이면 바로 추가
    if i.isalpha():
        res += i
    # 괄호 열면 스택에 추가
    elif i == '(':
        stack.append(i)
    # 곱셈이나 나눗셈이면 그 이전 계산들 내보내기
    elif i == '*' or i == '/':
        while stack and (stack[-1] == '*' or stack[-1] == '/'):
            res += stack.pop()
        stack.append(i)
    # 덧셈이나 뺄셈이면
    elif i == '+' or i == '-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(i)

    # 시작 괄호가 나올 때까지 스택 비우기
    elif i == ')':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.pop()  # ( 괄호 제거

# 스택 비우기
while stack:
    res += stack.pop()
print(res)
