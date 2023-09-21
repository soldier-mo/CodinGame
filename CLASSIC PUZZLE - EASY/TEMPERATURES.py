n = int(input())
closest_to_zero = 10000
for i in input().split():
    t = int(i)
    if abs(t) == abs(closest_to_zero) and t != closest_to_zero:
        closest_to_zero = abs(t)
    elif abs(t) < abs(closest_to_zero):
        closest_to_zero = t
print(closest_to_zero if closest_to_zero is not 10000 else 0)