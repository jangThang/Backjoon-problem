# 입력
N = int(input())

# 사면체에 필요한 포탄 수 계산
item = [1]  # 3, 6, 10, 15씩 늘어남
plus = 3  # 포탄이 늘어나는 개수
for i in range(300001):
    # 포탄 개수가 부족해지면 종료
    if item[i] >= N:
        break
    item.append(item[i] + plus)
    plus += (3+i)


# 사면체 개수 구하기 DP
cache = [3000000] * (N+1)
for i in range(1, N+1):
    for size in item:
        # 사면체에 필요한 포탄 수보다 적은 경우 break
        if size > i:
            break

        # 사면체에 필요한 포탄 수와 동일하면 1개
        elif size == i:
            cache[i] = 1
            break

        # 사면체에 필요한 포탄 수보다 많은 경우
        else:
            cache[i] = min(cache[i], 1 + cache[i-size])
print(cache[N])
