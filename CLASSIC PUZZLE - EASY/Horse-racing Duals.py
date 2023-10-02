inputs = []
min_d = float('inf')
for i in range(int(input())):
    inputs.append(int(input()))

inputs.sort()
for i in range(len(inputs)-1):
    d = inputs[i + 1] - inputs[i]
    if d < min_d:
        min_d = d
print(min_d)


#with inline loops
# inputs = [int(input()) for _ in range(int(input()))]
# inputs.sort()
# min_d = min(inputs[i + 1] - inputs[i] for i in range(len(inputs) - 1))
# print(min_d)
 