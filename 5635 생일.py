n = int(input())
student = []
for i in range(n):
    name, day, month, year = input().split()
    student.append([int(year), int(month), int(day), name])
student.sort()
print(student[n-1][3])
print(student[0][3])
