import sys
input = sys.stdin.readline

# 테스트케이스
T = int(input())
for _ in range(T):
    # 입력
    N = int(input())
    applicant = []
    for _ in range(N):
        applicant.append(list(map(int, input().split())))

    # 정렬(서류 기준 오름차순)
    applicant.sort()
    cut_line = applicant[0][1]  # 서류 1등의 면접 등수

    cnt = 1  # 합격자 수
    for i in applicant:
        # 서류는 앞 사람보다 낮지만, 면접 등수는 높은 참가자는 합격
        if cut_line > i[1]:
            cnt += 1
            cut_line = i[1]
    print(cnt)
