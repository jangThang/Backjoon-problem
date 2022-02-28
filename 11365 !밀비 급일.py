import sys
input = sys.stdin.readline

while True:
    sentence = input().rstrip()
    if sentence == 'END':
        break
    print(sentence[::-1])
