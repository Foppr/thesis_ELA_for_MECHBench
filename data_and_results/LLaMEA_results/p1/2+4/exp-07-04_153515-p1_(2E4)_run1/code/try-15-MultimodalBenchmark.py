import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add multiple local minima using combined sinusoidal perturbations
        for i in range(self.dim):
            f_val += 0.2 * np.sin(7 * x[i]) * np.cos(4 * x[i]) * np.sin(2 * x[i])
            
        # Add a more complex global minimum structure
        f_val += 0.1 * np.sum(np.sin(15 * x) * np.cos(10 * x))
        
        # Add a challenging landscape with varying amplitude
        f_val += 0.05 * np.sum((x**4) * np.sin(5 * x))
        
        return f_val