def combin(arr, k, index, current_combination):
    if len(current_combination) == k:
        print(current_combination)
        return
    for i in range(index, len(arr)):
        combin(arr, k, i + 1, current_combination+[arr[i]])
arr = list(map(int, input().split()))
k = int(input())
combin(arr, k, 0, [])