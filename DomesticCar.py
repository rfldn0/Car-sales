from Car import Car

class domestic_car(Car):
    def __init__(self, brand, model, year, price, type, state):
        #use super keyword
        super().__init__(brand, model, year, price, type)
        self.state = state

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state

    def print_info(self):
        pass
