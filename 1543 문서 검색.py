doc = input().rstrip()  # 문서
word = input().rstrip()  # 단어

cnt = 0  # 등장 횟수
idx = 0  # 문서의 철자 인덱스
while True:
    # 문서의 길이를 넘어서면, 탐색 종료
    if idx + len(word) > len(doc):
        break

    for i in range(len(word)):
        # 중간에 맞지 않으면 끊기
        if doc[idx+i] != word[i]:
            idx += 1
            break

    # 중간에 안 끊어졌으면 단어 1개 탐색 완료
    else:
        cnt += 1
        idx += len(word)
print(cnt)
