import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        f_value = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal perturbations
        for i in range(self.dim):
            f_value += 0.1 * np.sin(5 * x[i]) * np.cos(3 * x[i])
            
        # Add a second set of local minima
        for i in range(self.dim):
            f_value += 0.05 * np.sin(7 * x[i])**2
            
        return f_value