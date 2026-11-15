import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with quadratic base
        f_value = np.sum(x**2)
        
        # Add multiple local minima using high-frequency sinusoidal terms
        for i in range(self.dim):
            f_value += 0.2 * np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Add strong interaction terms between dimensions with non-linear coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_value += 0.12 * np.sin(5 * x[i] + 3 * x[j]) * np.cos(4 * x[i] - 2 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add cubic and quartic terms for increased nonlinearity and complexity
        for i in range(self.dim):
            f_value += 0.05 * x[i]**3 + 0.02 * x[i]**4
            
        # Add a multi-peak sinusoidal component to increase landscape ruggedness
        peak_term = 0.0
        for i in range(self.dim):
            peak_term += np.sin(8 * x[i]) * np.cos(6 * x[i])
        f_value += 0.15 * peak_term
        
        return f_value