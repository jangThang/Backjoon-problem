word = input()
for s in word:
    #A~C
    if ord(s) <= 67:
        print(chr(ord(s) - 3 + 26), end="")
    else:
        print(chr(ord(s)-3), end="")
