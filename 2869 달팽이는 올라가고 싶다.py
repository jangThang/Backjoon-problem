A, B, V = map(int, input().split())
#하루만에 다 올라감
if V < A:
    print(1)
else:
    day = (V-B) // (A-B) # V를 올라가는 데 걸리는 날짜 (정상에 도달하면 밤에 내려오는 B는 뺌)
    if (V-B) % (A-B) == 0:
        print(day)
    else: #나머지가 있으면 다음날에 완주
        print(day+1) 
