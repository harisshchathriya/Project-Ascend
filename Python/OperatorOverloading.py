class d:
    def __init__(self,a):
        self.a=a
    def __add__(self,other):
        return self.a+other.a
a=d(5)
b=d(10)
print(a+b)
