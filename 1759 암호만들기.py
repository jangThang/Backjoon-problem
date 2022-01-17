from itertools import combinations

L, C = map(int, input().split())
alphabet = list(input().split())
alphabet.sort()

arr = list(combinations(alphabet, L))
answer = list()
for lst in arr:
    vowels = 0
    consonants = 0
    for i in lst:
        if (i=='a') | (i=='e') | (i=='i') | (i=='o') | (i=='u'): 
            vowels += 1
        else:
            consonants += 1
    if (vowels > 0) & (consonants > 1):
        answer.append(''.join(lst))
        
for i in answer:
    print(i)
