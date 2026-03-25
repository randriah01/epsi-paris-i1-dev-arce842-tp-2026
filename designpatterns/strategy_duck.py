from abc import ABC, abstractmethod, abstractclassmethod

class QuackBehavior(ABC):
    
    @abstractmethod
    def quack(self):
        ...

class QuackQuack(QuackBehavior):
    
    def quack(self):
        print('Quack quack')
        
class SmallQuack(QuackBehavior):
    
    def quack(self):
        print('Small quack')

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

def add_publisher_feature(cls):
    #TODO: review quack
    return cls

@add_publisher_feature
class Duck(ABC):
    
    def __init__(self, fly_behavior:FlyBehavior, quack_behavior:QuackBehavior):
        self.__fly_behavior = fly_behavior
        self.__quack_behavior = quack_behavior
    
    def display(self):
        print(self.__class__.__name__, 'says hello')
    
    def set_fly_behavior(self, fly_behavior:FlyBehavior):
        self.__fly_behavior = fly_behavior
    
    def fly(self):
        self.__fly_behavior.fly()
        
    def set_quack_behavior(self, quack_behavior:QuackBehavior):
        self.__quack_behavior = quack_behavior
        
    def quack(self):
        self.__quack_behavior.quack()

def add_quack_counter_feature(duck : Duck) -> None:
    if 'counter' in duck.__dict__:
        duck.counter += 1
    else:
        duck.counter = 0
      
def add_quack_counter_feature_v2(cls=None, *, steps=1):
    def wrap_quack_counter(cls):
        class ChildCls(cls):
            def __init__(self):
                super().__init__()
                self.__counter = 0
                
            def quack(self):
                super().quack()
                self.__counter += steps
                
            @property
            def counter(self):
                return self.__counter
 
        return ChildCls
    
    if cls is None:
        return wrap_quack_counter
    else:
        return wrap_quack_counter(cls)



def add_fly_counter(duck : Duck) -> Duck:
    return duck

@add_quack_counter_feature_v2(steps=2)
class GreenDuck(Duck):
    
    def __init__(self):
        super().__init__(fly_behavior=FlyToTheMoon, quack_behavior=QuackQuack())

class MallardDuck(Duck):

    def __init__(self):
        super().__init__(fly_behavior=FlyBackward, quack_behavior=SmallQuack())


class OtherDuck(Duck):

    def __init__(self):
        super().__init__(fly_behavior=FlyToTheMoon, quack_behavior=SmallQuack())



if __name__ == '__main__':
    green_duck = GreenDuck()
    green_duck.display()
    green_duck.fly()
    green_duck.quack()
    green_duck.set_fly_behavior(FlyBackward)
    green_duck.fly()

    
    mallard = MallardDuck()
    mallard.display()
    mallard.fly()
    mallard.quack()
    mallard.set_quack_behavior(QuackQuack())
    mallard.quack()