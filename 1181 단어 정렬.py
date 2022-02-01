import sys
input = sys.stdin.readline

N = int(input())
wordlist = []
for i in range(N):
    word = input().rstrip()
    wordlist.append([len(word), word])

wordlist.sort()

tmp = ''
for i in wordlist:
    if tmp == i[1]:
        continue
    tmp = i[1]
    print(i[1])
