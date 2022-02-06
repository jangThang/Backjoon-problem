T = int(input())
quadrant = [0]*4 # 사분면
axis = 0 # 축
for i in range(T):
    x, y = map(int, input().split())

    # 축에 포함될 경우
    if x == 0 or y == 0:
        axis += 1
    # 1사분면
    elif x > 0 and y > 0:
        quadrant[0] += 1
    # 2사분면
    elif x < 0 and y > 0:
        quadrant[1] += 1
    # 3사분면
    elif x < 0 and y < 0:
        quadrant[2] += 1
    # 4사분면
    else:
        quadrant[3] += 1

#출력
print("Q1:", quadrant[0])
print("Q2:", quadrant[1])
print("Q3:", quadrant[2])
print("Q4:", quadrant[3])
print("AXIS:", axis)
