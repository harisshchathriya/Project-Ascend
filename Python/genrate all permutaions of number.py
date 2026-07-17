def permute(l,i):
    if i==len(l):
        print(l)
        return
    for j in range(i,len(l)):
        l[i],l[j]=l[j],l[i]
        permute(l,i+1)
        l[i],l[j]=l[j],l[i]
l=list(map(int,input().split()))
permute(l,0)