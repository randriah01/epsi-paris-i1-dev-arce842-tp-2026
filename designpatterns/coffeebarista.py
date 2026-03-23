from abc import ABC, abstractmethod

# milk cost: 0.5
# sugar cost: 0.4

class Beverage(ABC):
    
    def __init__(self):
        self.milk = None
        self.sugar = None
        self.cookies = None

        
    def add_milk(self):
        self.milk = Milk()
        
    def add_sugar(self):
        self.sugar = Sugar()
        
    def add_cookies(self):
        self.cookies = Cookies()
    
    def cost(self):
        total_cost = 0
        if self.milk:
            total_cost += self.milk.cost()
        if self.sugar:
            total_cost += self.sugar.cost()
        if self.cookies:
            total_cost += self.cookies.cost()
        return total_cost

# base cost: 1        
class Coffee(Beverage):
    
    def __init__(self):
        super().__init__()
        self.coffee_bean = None
    
    def add_coffee_bean(self):
        self.coffee_bean = CoffeeBean()
    
    def cost(self):
        total_cost = 1.0 + super().cost()
        if self.coffee_bean:
            total_cost += self.coffee_bean.cost()
        return total_cost

# base cost: 1.5    
class Tea(Beverage):

    def __init__(self):
        super().__init__()
        
    def cost(self):
        total_cost = 1.5 + super().cost()
        return total_cost
        
# base cost: 0.7
class Chocolate(Beverage):
    
    def __init__(self):
        super().__init__()
        self.sha = None

    def add_sha(self):
        self.sha = Sha()

    def cost(self):
        total_cost = 0.7 + super().cost()
        if self.sha:
            total_cost += self.sha.cost()
        return total_cost

# base cost: 2.0    
class Latte(Beverage):

    def __init__(self):
        super().__init__()
        self.sha = None

    def add_sha(self):
        self.sha = Sha()

    def cost(self):
        total_cost = 2.0 + super().cost()
        if self.sha:
            total_cost += self.sha.cost()
        return total_cost    

class Condiment(ABC):
    
    @abstractmethod
    def cost(self):
        ...
        
class Sugar(Condiment):
    
    def cost(self):
        return 0.4
    
class Milk(Condiment):
    
    def cost(self):
        return 0.5
    
class Cookies(Condiment):
    
    def cost(self):
        return 0.64

class CoffeeBean(Condiment):
    
    def cost(self):
        return 0.2
    
class Sha(Condiment):
    
    def cost(self):
        return 0.5

if __name__ == '__main__':
    c = Coffee()
    print(f'Coffee dark {c.cost()}')
    c.add_sugar()
    print(f'Coffee sugar {c.cost()}')
    tea = Tea()
    tea.add_milk()
    print(f'Tea light {tea.cost()}')
    
    # nouvelle version
    
    c = Milk(Sugar(Coffee()))
    print(f'Coffee milk sugar {c.cost()}')
