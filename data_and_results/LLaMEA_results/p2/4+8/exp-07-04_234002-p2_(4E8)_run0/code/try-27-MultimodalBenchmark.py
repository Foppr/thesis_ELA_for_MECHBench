import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for global minimum at origin
        f_value = np.sum(x**2)
        
        # Add multiple local minima using combined sinusoidal and cubic terms
        for i in range(self.dim):
            f_value += 0.2 * np.sin(3 * x[i]) * np.cos(2 * x[i]) + 0.05 * x[i]**3
            
        # Add challenging cross-dimensional interactions with higher frequency components
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.1 * np.sin(4 * x[i] + 2 * x[j]) * np.cos(3 * x[i] - x[j]) + 0.02 * (x[i] * x[j])**2
        
        # Add a secondary sinusoidal landscape to increase complexity
        f_value += 0.15 * np.sum(np.sin(0.5 * x) * np.cos(0.3 * x))
        
        return f_value