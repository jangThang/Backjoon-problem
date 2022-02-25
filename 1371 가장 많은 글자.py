import sys
sentence = sys.stdin.read()
word = [0]*26 #a~z

for i in sentence:
    if i.islower():
        word[ord(i)-97] += 1
for i in range(26):
    if word[i] == max(word):
        print(chr(i+97), end="")
