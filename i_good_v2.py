from abc import ABC, abstractmethod

class Vehicle(ABC):
    @abstractmethod
    def go(self):
        pass
    
class Flyable(Vehicle):
    @abstractmethod
    def fly(self):
        pass
    
class Aircraft(Flyable):
    def go(self):
        print("Taxiing")
    def fly(self):
        print("Flying")

class Car(Vehicle):
    def go(self):
        print("Going")
    
if __name__ == '__main__':
    airbus = Aircraft()
    airbus.go()
    airbus.fly()
    
    f1 = Car()
    f1.go()
