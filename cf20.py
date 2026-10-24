n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()
mid = n // 2

current = a[mid]

for i in range(mid + 1, n):
    diff = a[i] - a[i - 1]
    cost = diff * (i - mid)
    
    if cost <= k:
        k -= cost
        current = a[i]
    else:
        current += k // (i - mid)
        print(current)
        exit()


current += k // (n - mid)
print(current)
