n = int(input())
for _ in range(n):
    string = input().lower()  # 대소문자 구분하지 않음
    
    # 팰린드롬 판별
    if string == string[::-1]:
        print("Yes")
    else:
        print("No")
