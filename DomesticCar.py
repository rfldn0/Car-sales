from Car import Car

class domestic_car(Car):
    def __init__(self, brand, model, year, price, type, state):
        #use super keyword
        super().__init__(brand, model, year, price, type)
        self.__state = state

    def get_state(self):
        return self.__state

    def set_state(self, state):
        self.__state = state

    def print_info(self):
        return super().print_info() + f" {self.__state}"
