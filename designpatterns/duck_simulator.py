from strategy_duck import Duck

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
        
    def quack(self):
        self.honk()

        
if __name__ == '__main__':
    goose = Goose()
    simulator = DuckSimulator()
    simulator.simulate(goose)