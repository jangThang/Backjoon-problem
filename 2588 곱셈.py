a = int(input())
b = int(input())

num = b
for i in range(3):
    print( (num%10)*a )
    num //= 10
print(a*b)
