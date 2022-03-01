#입력
s = input()
find = 'UCPC' #찾아야할 문자열
idx = 0
for i in s:
    # 해당 글자를 찾았으면 다음 글자로 넘어감
    if i == find[idx]:
        idx += 1
    # UCPC를 모두 찾았으면 끝내기
    if idx == 4:
        print("I love UCPC")
        break
else:
    print("I hate UCPC")
