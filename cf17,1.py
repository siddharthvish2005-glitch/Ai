n=int(input())
a=list(map(int,input().split()))
m=int(input())
b=list(map(int,input().split()))
list=[]
total =0
for i in a:
    total+=i
    list.append(total)

for q in b:
    left =0
    right =n-1
    while left<=right:
        mid=(left +right)//2

        if list[mid]>=q:
            right=mid-1
        else:
            left=mid+1

    print(left+1)
