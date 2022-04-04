import sys
input = sys.stdin.readline

# 입력
N = int(input())
book_dict = {}

for _ in range(N):
    book = input().rstrip()

    # 이미 등록된 책이면 1개 추가
    if book in book_dict:
        book_dict[book] += 1

    # 등록되지 않은 책이면 새로 등록
    else:
        book_dict[book] = 1

# 판매량이 많은 순으로 정렬
res = list(book_dict.items())
res.sort(key=lambda x: (-x[1], x[0]))

print(res[0][0])
