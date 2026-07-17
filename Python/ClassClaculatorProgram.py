class claci:
    def add(self,a,b):
        return a+b
    def sub(self,a,b):
        return a-b
    def mul(self,a,b):
        return a*b
    def div(self,a,b):
        if b==0:
            return "Error" 
        return a/b
    def mod(self,a,b):
        if b==0:
            return "Error"
        return a%b
    def pow(self,a,b):
        return a**b
    def fdiv(self,a,b):
        if b==0:
            return "Error" 
        return a//b
    def display(self):
        if n==1:
            print(c.add(a,b))
        elif n==2:
            print(c.sub(a,b))
        elif n==3:
            print(c.mul(a,b))
        elif n==4:
            print(c.div(a,b))
        elif n==5:
            print(c.mod(a,b))
        elif n==6:
            print(c.pow(a,b))
        elif n==7:
            print(c.fdiv(a,b))
        
n=int(input())
a=int(input())
b=int(input())
c=claci()
c.display()


