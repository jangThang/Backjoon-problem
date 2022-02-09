import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
numlist = list(map(int, input().split()))
M = int(input())
findlist = list(map(int, input().split()))

count = Counter(numlist)
for i in range(len(findlist)):
    if findlist[i] in count:
        print(count[findlist[i]], end=' ')
    else:
        print(0, end=' ')
        
        
# import sys
# input = sys.stdin.readline

# N = int(input())
# numlist = list(map(int, input().split()))
# M = int(input())
# findlist = list(map(int, input().split()))

# #이진 탐색(자료, 찾는 값)
# def binarySearch(lst, x):
#     start = 0
#     end = len(lst)-1

#     while start <= end:
#         mid = (start + end)//2 # 중앙위치
#         if x == lst[mid]: # 중앙값이 찾는 값
#             cnt = 1 # 찾은 개수

#             left = 1 # 왼쪽에 동일한 값 찾기
#             while mid-left >= 0 and x == lst[mid-left]:
#                 cnt += 1
#                 left += 1

#             right = 1 # 오른쪽에 동일한 값 찾기
#             while mid + right < len(lst) and x == lst[mid + right]:
#                 cnt += 1
#                 right += 1
#             return cnt

#         elif x > lst[mid]: # 중앙값보다 큰 경우
#             start = mid + 1
#         else:
#             end = mid - 1 # 중앙값보다 작은 경우
#     return 0 # 찾지 못한 경우

# # 정렬
# numlist.sort()
# for i in findlist:
#     print(binarySearch(numlist, i), end=" ")
