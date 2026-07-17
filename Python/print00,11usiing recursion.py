def print_numbers(n,p=""):
    if len(p)==n:
        print(p)
        return
    print_numbers(n,p+"0")
    print_numbers(n,p+"1")
n=int(input())
print_numbers(n)