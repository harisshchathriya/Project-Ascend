def UglyNumber(a):
    while a%5==0:
        a//=5
    while a%3==0:
        a//=3
    while a%2==0:
        a//=2
    return "Yes" if a===1 else "No"
x=int(input())
