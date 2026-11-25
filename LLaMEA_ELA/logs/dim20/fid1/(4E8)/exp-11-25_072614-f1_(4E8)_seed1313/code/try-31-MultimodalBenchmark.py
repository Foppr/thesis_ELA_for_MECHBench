import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations to create multiple local minima
        sinusoidal = np.sum(np.sin(5.0 * x)) + 0.5 * np.sum(np.sin(10.0 * x)) + 0.1 * np.sum(np.sin(15.0 * x))
        
        # Exponential perturbations to increase landscape complexity
        exponential = np.sum(np.exp(-0.5 * x**2)) + 0.3 * np.sum(np.exp(-x**2))
        
        # Combined function with global minimum at origin
        return polynomial + sinusoidal + exponential + 0.05 * np.sum(x**8)