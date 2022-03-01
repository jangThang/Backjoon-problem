import sys
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    s1, s2 = input().rstrip().split()
    a = sorted(s1)
    b = sorted(s2)
    if a == b:
        print(s1, '&', s2, "are anagrams.")
    else:
        print(s1, '&', s2, "are NOT anagrams.")
