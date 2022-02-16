regulation = int(input())
speed = int(input())

diff = speed - regulation
# 31초과
if diff > 30:
    print("You are speeding and your fine is $500.")
# 21초과
elif diff > 20:
    print("You are speeding and your fine is $270.")
# 초과
elif diff > 0:
    print("You are speeding and your fine is $100.")
# 규정준수
else:
    print("Congratulations, you are within the speed limit!")
