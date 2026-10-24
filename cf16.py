n=int(input())
arr=list(map(int,input().split()))
m=max(arr)
mn=min(arr)
max_pos=arr.index(m)
min_pos=arr.index(mn)
min_pos=n-1-arr[::-1].index(mn)
swaps=0
swaps=max_pos+(n-1-min_pos)
  
if (max_pos>min_pos):
    swaps -=1

print(swaps)    