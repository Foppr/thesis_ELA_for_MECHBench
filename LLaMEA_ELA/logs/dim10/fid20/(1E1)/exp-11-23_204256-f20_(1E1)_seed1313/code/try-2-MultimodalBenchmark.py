import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Add sinusoidal perturbations with different frequencies to create multiple local minima
        f2 = 0.15 * np.sum(np.sin(7 * np.pi * x_normalized) ** 2)
        
        # Add a global scaling factor to control the function landscape
        f3 = 0.02 * np.sum(x_normalized**4)
        
        # Add cubic terms to increase complexity and create sharper local optima
        f4 = 0.05 * np.sum(x_normalized**3)
        
        return f1 + f2 + f3 + f4