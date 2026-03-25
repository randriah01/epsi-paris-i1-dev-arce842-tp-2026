from strategy_duck import Duck, FlyBehavior, QuackBehavior
from strategy_duck import GreenDuck, MallardDuck, OtherDuck
from abc import ABC, abstractmethod

class DuckSimulator:
    
    def simulate(self, duck : Duck):
        if not isinstance(duck, Duck):
            print('Error, this is not a duck')
            return
        self.__fly_n_times(duck, 2)
        duck.quack() #ERROR: fix this in 2 lines
        self.__fly_n_times(duck, 3)
        
    def __fly_n_times(self, duck : Duck, n_times : int):
        for _ in range(n_times):
            duck.fly()

class Goose:
    
    def honk(self):
        print('Honk honk')
        
    def fly(self):
        print('Fly like a goose')
        
    # def quack(self):
    #     self.honk()

# Adapter
class DuckDisguiseGreen(Duck):

    def __init__(self, goose : Goose):
        super().__init__(None, None)
        self.goose = goose

    def fly(self):
        self.goose.fly()
        
    def quack(self):
        self.goose.honk()

class GooseFly(FlyBehavior):
    
    def __init__(self, goose : Goose):
        self.goose = goose
        
    def fly(self):
        self.goose.fly()
        
class GooseQuack(QuackBehavior):
    
    def __init__(self, goose : Goose):
        self.goose = goose
        
    def quack(self):
        self.goose.honk()

class DuckDisguiseBanana(Duck):
    
    def __init__(self, goose : Goose):
        super().__init__(GooseFly(goose), GooseQuack(goose))

# def / return ??
# class
# Decorator Quack Counter
class QuackCounter(Duck):
    
    def __init__(self, duck : Duck):
        super().__init__(duck._Duck__fly_behavior, duck._Duck__quack_behavior)
        self.__duck = duck
        self.__counter = 0
        
    def quack(self):
        self.__duck.quack()
        self.__counter += 1
        
    @property
    def counter(self):
        return self.__counter

class QuackCounterBehavior(QuackBehavior):
    
    def __init__(self, duck_quack : QuackBehavior):
        self.__duck_quack = duck_quack
        self.__counter = 0
    
    def quack(self):
        self.__duck_quack.quack()
        self.__counter += 1
        
    @property
    def counter(self):
        return self.__counter

class QuackCounterV2(Duck):
    
    def __init__(self, duck : Duck):    
        super().__init__(duck._Duck__fly_behavior,
                         QuackCounterBehavior(duck._Duck__quack_behavior))
        self.__duck = duck
        
    @property
    def counter(self):
        return self._Duck__quack_behavior.counter

class Observer(ABC):
    
    @abstractmethod
    def notify(self, subject):
        ...

class Quackologist(Observer):
    
    def __init__(self):
        self.__total_quacks = 0
    
    def notify(self, subject):
        print('#TODO')

if __name__ == '__main__':
    goose = Goose()
    donald = GreenDuck()
    fifi = MallardDuck()
    leonardo = OtherDuck()
    simulator = DuckSimulator()
    # simulator.simulate(DuckDisguiseGreen(goose))
    # simulator.simulate(DuckDisguiseBanana(goose))
    fifi = QuackCounter(fifi)
    simulator.simulate(fifi)
    simulator.simulate(fifi)
    leonardo = QuackCounterV2(leonardo)
    for _ in range(10):
        simulator.simulate(donald)
    # simulator.simulate(leonardo)
    # simulator.simulate(leonardo)
    # display the number of times a duck quacked
    # add_quack_counter_feature(donald)
    print(f'Counter donald: {donald.counter}')
    print(f'Counter fifi: {fifi.counter}')
    print(f'Counter leonardo: {leonardo.counter}')