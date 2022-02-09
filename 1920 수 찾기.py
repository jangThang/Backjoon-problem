N = int(input())
numlist = list(map(int, input().split()))
M = int(input())
findlist = list(map(int, input().split()))

#이진 탐색(자료, 찾는 값)
def binarySearch(lst, x):
    start = 0
    end = len(lst)-1

    while start <= end:
        mid = (start + end)//2 # 중앙위치
        if x == lst[mid]: # 중앙값이 찾는 값
            return 1 # 찾았음
        elif x > lst[mid]: # 중앙값보다 큰 경우
            start = mid + 1
        else:
            end = mid - 1 # 중앙값보다 작은 경우
    return 0 # 찾지 못한 경우

# 정렬
numlist.sort()
for i in findlist:
    print(binarySearch(numlist, i))
