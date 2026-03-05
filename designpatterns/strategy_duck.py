from abc import ABC, abstractmethod, abstractclassmethod

class FlyBehavior(ABC):
    
    @abstractclassmethod
    def fly(self):
        ...

class FlyToTheMoon(FlyBehavior):
    
    @classmethod
    def fly(self):
        print('Fly to the moon')

class FlyBackward(FlyBehavior):
    
    @classmethod
    def fly(self):
        print('Backward flying')


class Duck(ABC):
    
    def __init__(self, fly_behavior:FlyBehavior):
        self.__fly_behavior = fly_behavior
    
    @abstractmethod
    def display(self):
        ...
        
    def fly(self):
        self.__fly_behavior.fly()

    
class GreenDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyToTheMoon())

    def display(self):
        print('Greenduck says hello')
    
    def quack(self):
        print('Quack quack')
    
class MallardDuck(Duck):

    def __init__(self):
        super().__init__(fly_behavior=FlyBackward())

    def display(self):
        print('MallardDuck says hello')
    
    def quack(self):
        print('Small quack')

class OtherDuck(Duck):

    def __init__(self):
        super().__init__(fly_behavior=FlyToTheMoon())
    
    def display(self):
        print('OtherDuck says hello')
        
    def quack(self):
        print('Small quack')