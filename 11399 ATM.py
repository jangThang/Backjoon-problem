N = int(input())
waiting = list(map(int, input().split()))

# 정렬
waiting.sort()

time = 0 #기다리는 시간
total = 0 #기다리는 총 시간
for t in waiting:
    total += (time + t) #여태까지 기다린 시간 + 인출하는 시간
    time += t #t만큼 시간 지남
print(total)
