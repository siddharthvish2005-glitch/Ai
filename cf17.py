import bisect
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
    pile=bisect.bisect_left(list,q)  
    print(pile+1)  

     


   