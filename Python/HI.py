a=int(input())
lst=list(map(int,input().split()))
for i in range(a-1):
    if lst[i]>lst[a-i-1]:
        lst[i],lst[i+1]=lst[i+1],lst[i]
print(lst)