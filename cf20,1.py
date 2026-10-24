n,k=map(int,input().split())
a=list(int,input().split())

a.sort()
mid=n//2
low=a[mid]
high=a[mid]+k

def can_make(x):
    ops=0
    for i in range(mid,n):
        if a[i]<x:
            ops+=x-a[i]
        if ops>k:
            return False
    return True            


while low<=high:
     mid_val=(low+high)//2 
     if can_make(mid_val):
        ans=mid_val
        low=mid_val+1
     else:
        high=mid_val-1


print(high)        
       
