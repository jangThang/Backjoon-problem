import itertools

N, M = map(int, input().split())
card = list(map(int, input().split()))

case = list(itertools.combinations(card, 3)) # N장의 카드 중 3장 선택할 경우의 수

res = 0
for i in case:
    if M-sum(i) >= 0 and res < sum(i): #M을 넘지 않으면서, 여태까지의 최댓값보다 크면 갱신
        res = sum(i)
print(res)
