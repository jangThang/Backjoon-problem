import sys
input = sys.stdin.readline

N, M = map(int, input().split())
# 입력

lst = [] #이름 저장
dict = dict() #번호랑 이름 매칭
for i in range(N):
    lst.append(input().rstrip())
    dict[lst[i]] = i+1 #포켓몬 이름, 번호

#출력
for i in range(M):
    question = input().rstrip()

    # 숫자면 list에서 탐색
    if question.isdigit():
        print(lst[int(question)-1])
    else:
        print(dict[question])
