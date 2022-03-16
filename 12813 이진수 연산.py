# 입력
A = map(int, input())
B = map(int, input())

# 계산
_and, _or, _xor, _notA, _notB = '', '', '', '', ''
for a, b in zip(A, B):
    _and += str(a and b) # A & B
    _or += str(a or b)
    _xor += str(a ^ b)
    _notA += str(int(not a))
    _notB += str(int(not b))

# 출력
print(_and)
print(_or)
print(_xor)
print(_notA)
print(_notB)
