#Object van intrect with each other
class Engine:
    def start(self):
        print("Engine started")
class Car:
    def __init__(self):
        self.engine=Engine()
    def drive(self):
        self.engine.start()
c=Car()
c.drive()