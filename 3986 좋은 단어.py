import sys
input = sys.stdin.readline

# 입력
n = int(input())
cnt = n  # 좋은 단어의 개수
for _ in range(n):
    text = input().rstrip()
    stack = []

    for s in text:
        # 이전 글자와 같으면 뺀다
        if stack and stack[-1] == s:
            stack.pop()

        # 이전 문자와 같지 않으면 넣는다
        else:
            stack.append(s)

    # 끝나고 stack이 남아있으면 좋은 단어가 아님
    if stack:
        cnt -= 1
print(cnt)
