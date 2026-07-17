num=[1,2,3,4]
res=list(map(lambda x:x**2,num))
print(res)

num=[1,2,3,4]
res=list(map(lambda x:x%2==0,num))
print(res)

n=["apple","banana","kiwi"]
res=sorted(n,key=len)
print(res)