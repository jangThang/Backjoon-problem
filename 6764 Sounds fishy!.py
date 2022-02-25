high = []
for _ in range(4):
    high.append(int(input()))

#증가
if high[0]<high[1]<high[2]<high[3]:
    print("Fish Rising")
#감소
elif high[0]>high[1]>high[2]>high[3]:
    print("Fish Diving")
#일정
elif high[0] == high[1] == high[2] == high[3]:
    print("Fish At Constant Depth")
#그 외
else:
    print("No Fish")
