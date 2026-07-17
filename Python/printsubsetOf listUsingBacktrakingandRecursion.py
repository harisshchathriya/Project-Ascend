def print_subsets(arr,i,s):
    if i==len(arr):
        print(s)
        return
    print_subsets(arr,i+1,s+[arr[i]])
    print_subsets(arr,i+1,s)
arr =list(map(int,input().split()))
print_subsets(arr,0,[])