l=list(map(int,input().split()))
s=[]
s1=[]
for i in range(len(l)):
    while s and l[s[-1]]<=l[i]:
        s.pop()
    if not s:
        s1.append(i+1)
    else:
        s1.append(i-s[-1])
    s.append(i)
print(s1) 