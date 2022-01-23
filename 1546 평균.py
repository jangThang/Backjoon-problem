n = int(input())
score = list(map(int, input().split()))
print( sum(score)/max(score)/n*100 )
