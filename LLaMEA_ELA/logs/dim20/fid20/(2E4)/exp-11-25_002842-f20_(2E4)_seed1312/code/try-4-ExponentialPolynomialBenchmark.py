import numpy as np

class ExponentialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Exponential decay component creating rugged regions
        exp_component = np.sum(np.exp(-0.5 * (x**2)) * np.cos(3 * x))
        
        # Polynomial valley component creating smooth regions
        poly_component = 0.1 * np.sum(x**4 - 2 * x**2)
        
        # Mixed sinusoidal-exponential term for additional complexity
        mixed_component = 0.05 * np.sum(np.sin(x) * np.exp(-0.1 * x**2))
        
        # Add a global quadratic penalty to ensure convergence
        penalty = 0.01 * np.sum(x**2)
        
        return exp_component + poly_component + mixed_component + penalty