import sys
input = sys.stdin.readline

score = 0
num = 0
for _ in range(20):
    _, credit, grade = input().rstrip().split()

    if grade == 'A+':
        score += float(credit)*4.5
    elif grade == 'A0':
        score += float(credit)*4
    elif grade == 'B+':
        score += float(credit)*3.5
    elif grade == 'B0':
        score += float(credit)*3.0
    elif grade == 'C+':
        score += float(credit)*2.5
    elif grade == 'C0':
        score += float(credit)*2.0
    elif grade == 'D+':
        score += float(credit)*1.5
    elif grade == 'D0':
        score += float(credit)*1.0
    elif grade == 'F':
        pass

    if grade == 'P':
        pass
    else:
        num += float(credit)
print(score/num)
