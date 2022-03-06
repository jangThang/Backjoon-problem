from collections import deque
import sys
input = sys.stdin.readline

#입력
T = int(input())
for _ in range(T):
    p = input().rstrip()
    n = int(input())
    if n == 0:
        input()
        numlist = deque([])
    else:
        numlist = deque(list(input().strip("[]\n").split(",")))
    #연산시작
    front = True #앞에서부터 제거
    for op in p:
        # 뒤집기
        if op =='R':
            #Toggle
            if front:
                front = False
            else:
                front = True
        # 버리기
        else:
            #빈 리스트가 아님
            if numlist:
                #앞에서부터 꺼내기
                if front:
                    numlist.popleft()
                #뒤에서부터 꺼내기
                else:
                    numlist.pop()
            #빈 배열임
            else:
                print("error")
                break

    #error없이 모든 연산을 마침
    else:
        if front:
            #앞쪽으로 모든 배열 꺼내기
            lst = ",".join(list(numlist))

        else:
            #뒤쪽으로 모든 배열 꺼내기
            lst = ",".join(list(numlist)[::-1])
        print(f"[{lst}]")
