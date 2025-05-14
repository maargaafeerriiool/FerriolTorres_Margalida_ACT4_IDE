class Vehicle:
    def __init__(self, marca):
        self.marca = marca

class Cotxe(Vehicle):
    def __init__(self, marca, model):
        super().__init__(marca)
        self.model = model
        self.motor = None

class Motor:
    def __init__(self, tipus):
        self.tipus = tipus

class Camio(Vehicle):
    def __init__(self, marca, capacitat):
        super().__init__(marca)
        self.capacitat = capacitat