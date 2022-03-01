import sys
input = sys.stdin.readline

#입력
while True:
    sentence = input().rstrip()
    if sentence == '#':
        break
    res = 0
    for i in sentence.lower():
        if i=='a' or i=='e' or i=='i' or i=='o' or i=='u':
            res += 1
    print(res)
