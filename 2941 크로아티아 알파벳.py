croatia = input()
cnt = len(croatia)
pre = '' #이전 글자
ppre = '' #이전 이전글자
for i in croatia:
    if i == '-':
        cnt -= 1
    if i == '=':
        cnt -= 1
        if pre == 'z' and ppre == 'd':
            cnt -= 1
    if i == 'j' and (pre == 'l' or pre == 'n'):
        cnt -= 1
    ppre = pre
    pre = i
print(cnt)
