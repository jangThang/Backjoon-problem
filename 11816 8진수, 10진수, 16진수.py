x = input()
if len(x) == 1:
    print(x)

elif x[0:2] == '0x':
    print(int(x[2:], 16))

elif x[0] == '0':
    print(int(x[1:], 8))

else:
    print(x)
