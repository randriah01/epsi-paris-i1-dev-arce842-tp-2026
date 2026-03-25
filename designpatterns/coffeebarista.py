from abc import ABC

# milk cost: 0.5
# sugar cost: 0.4

class Beverage(ABC):
    

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

    def cost(self):
        return 1.0

# base cost: 1.5    
class Tea(Beverage):


    def cost(self):
        return 1.5
        
# base cost: 0.7
class Chocolate(Beverage):
    
    def cost(self):
        return 0.7

# base cost: 2.0    
class Latte(Beverage):

    def cost(self):
        return 2.0    

class Condiment(Beverage):
    
    def __init__(self, beverage):
        super().__init__()
        self.beverage = beverage
    
    def cost(self):
        return self.beverage.cost()
        
class Sugar(Condiment):
    
    def __init__(self, beverage):
        super().__init__(beverage)
    
    def cost(self):
        return 0.4 + self.beverage.cost()
    
class Milk(Condiment):

    def __init__(self, beverage):
        super().__init__(beverage)

    
    def cost(self):
        return 0.5 + self.beverage.cost()
    
class Cookies(Condiment):

    def __init__(self, beverage):
        super().__init__(beverage)

    
    def cost(self):
        return 0.64 + self.beverage.cost()

class CoffeeBean(Condiment):

    def __init__(self, beverage):
        super().__init__(beverage)

    
    def cost(self):
        return 0.2 + self.beverage.cost()
    
class Sha(Condiment):

    def __init__(self, beverage):
        super().__init__(beverage)
    
    def cost(self):
        return 0.5 + self.beverage.cost()

class Cloud(Condiment):
    
    def __init__(self, beverage):
        super().__init__(beverage)
    
    def cost(self):
        return 12.3 + self.beverage.cost()
    

if __name__ == '__main__':
    # c = Coffee()
    # print(f'Coffee dark {c.cost()}')
    # c.add_sugar()
    # print(f'Coffee sugar {c.cost()}')
    # tea = Tea()
    # tea.add_milk()
    # print(f'Tea light {tea.cost()}')
    
    # nouvelle version
    
    # Decorator
    dark_coffee = Coffee()
    print(f'Dark Coffee {dark_coffee.cost()}')
    
    c = Sugar(Cloud(Coffee()))
    #type (Sugar(Coffee)) == type(Coffee)
    print(f'Coffee cloud sugar {c.cost()}')
    
    t = Sugar(Milk(Tea()))
    print(f'Tea milk sugar {t.cost()}')

