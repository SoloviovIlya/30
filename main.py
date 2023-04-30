a1 = int(input())
d = int(input())
n = int(input())
progressive = [a1 + (i - 1) * d for i in range(1, n + 1)]
print(*progressive)