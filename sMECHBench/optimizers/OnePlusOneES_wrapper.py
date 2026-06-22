from .jacob.algorithms.one_plus_one_es import OnePlusOneES

class OnePlusOneESWrapper:
    def __init__(self, f, budget):
        self.f = f
        self.optimizer = OnePlusOneES(budget=budget)

    def run(self):
        return self.optimizer(self.f)