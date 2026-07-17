from abc import ABC, abstractmethod
class student(ABC):
    @abstractmethod
    def display(self):
        pass
class details(student):
    def __init__(self,name,age,):
        self.name=name
        self.age=age
    def display(self):
        print("Name:",self.name)
        print("Age:",self.age)
n=int(input())
l=[]
for i in range(n):
    a=input()
    b=int(input())
    s=details(a,b)
    l.append(s)
for i in l:
    i.display()