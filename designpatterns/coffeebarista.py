from abc import ABC, abstractmethod

# milk cost: 0.5
# sugar cost: 0.4

class Beverage(ABC):
    
    def __init__(self):
        self.milk = False
        self.sugar = False
        
        
    def add_milk(self):
        self.milk = True
        
    def add_sugar(self):
        self.sugar = True
    
    @abstractmethod
    def cost(self):
        ...

# base cost: 1        
class Coffee(Beverage):
    
    def __init__(self):
        super().__init__()
        self.coffee_bean = False
    
    def add_coffee_bean(self):
        self.coffee_bean = True
    
    def cost(self):
        total_cost = 1.0
        if self.milk:
            total_cost += 0.5
        if self.sugar:
            total_cost += 0.4
        if self.coffee_bean:
            total_cost += 0.2
        return total_cost

# base cost: 1.5    
class Tea(Beverage):

    def __init__(self):
        super().__init__()
        
    def cost(self):
        total_cost = 1.5
        if self.milk:
            total_cost += 0.5
        if self.sugar:
            total_cost += 0.4
        return total_cost
        
# base cost: 0.7
class Chocolate(Beverage):
    
    def __init__(self):
        super().__init__()
        self.sha = False

    def add_sha(self):
        self.sha = True

    def cost(self):
        total_cost = 0.7
        if self.milk:
            total_cost += 0.5
        if self.sugar:
            total_cost += 0.4
        if self.sha:
            total_cost += 0.5
        return total_cost

# base cost: 2.0    
class Latte(Beverage):

    def __init__(self):
        super().__init__()
        self.sha = False

    def add_sha(self):
        self.sha = True

    def cost(self):
        total_cost = 2.0
        if self.milk:
            total_cost += 0.5
        if self.sugar:
            total_cost += 0.4
        if self.sha:
            total_cost += 0.5
        return total_cost    
    
if __name__ == '__main__':
    c = Coffee()
    print(c.cost())
    c.add_sugar()
    print(c.cost())
    tea = Tea()
    tea.add_milk()
    print(tea.cost())
