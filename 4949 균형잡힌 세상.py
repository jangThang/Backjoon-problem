import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == '.':
        break

    check = True # 균형파괴 유무
    pre = [] # 이전 괄호 기록
    for s in sentence:
        # 스택구조로 여는 괄호 보관
        if s == '(' or s == '[':
            pre.append(s)
            
        # 스택에서 하나씩 꺼내면서, 괄호짝 확인
        elif s == ')':
            if len(pre) == 0 or '(' != pre.pop():
                check = False
                break
        elif s == ']':
            if len(pre) == 0 or '[' != pre.pop():
                check = False
                break

    # 남은 열린 괄호가 없고 짝이 다 맞았으면 yes 아니면 no
    if check and len(pre) == 0:
        print("yes")
    else:
        print("no")
