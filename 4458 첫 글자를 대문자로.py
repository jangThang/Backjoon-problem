T = int(input())
for i in range(T):
    s = list(input().split())
    res = ''
    for word in s:
        if word == 'of' or word == 'and':
            res += word + ' '
        else:
            res += word[0].upper() + word[1:] + ' '
    print(res[:-1])
