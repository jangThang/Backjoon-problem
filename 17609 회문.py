import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s = input().rstrip()
    left = False
    right = False
    # 한 칸씩 당기며 앞과 뒤를 비교
    for i in range(len(s) // 2):
        #앞뒤 문자가 맞지 않음
        if s[i] != s[len(s) - 1 - i]:
            #맨 가운데 비교이고 아직 틀린 게 없으면 유사회문
            if len(s) - 1 - i*2 == 1 and not left and not right:
                print(1)
                break
            # 앞 글자 삭제 후 계속해서 비교
            for j in range(i, len(s)//2):
                # 그 후로도 또 맞지 않는 문자가 있으면 앞쪽 제거로는 유사회문 못 만듬
                if s[j + 1] != s[len(s) - 1 - j]:
                    left = True

            # 뒤 글자 삭제 후 계속해서 비교
            for j in range(i, len(s)//2):
                # 그 후로도 또 맞지 않는 문자가 있으면 뒤쪽 제거로는 유사회문 못 만듬
                if s[j] != s[len(s) - 1 - j - 1]:
                    right = True

            # 앞과 뒤가 둘 다 안맞으면 회문이 아님
            if left and right:
                print(2)
                break
            # 앞 또는 뒤 중 1쪽을 빼면 회문이 됨 = 유사회문
            elif left or right:
                print(1)
                break
    #앞뒤가 다 맞았으면 회문
    else:
        print(0)
