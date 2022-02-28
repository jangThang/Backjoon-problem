import sys
input = sys.stdin.readline

#입력
N = int(input())
alphabet = [0]*26
for _ in range(N):
    name = input()
    alphabet[ord(name[0])-97] += 1

#5명 이상이면 출력
res = ''
for i, char in enumerate(alphabet):
    if char >= 5:
        res += chr(i+97)

#아무도 없으면 항복
if res == '':
    print("PREDAJA")
else:
    print(res)
