import numpy as np

class CorrelatedRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Exponentially decaying correlations between dimensions
        for i in range(self.dim):
            f_val += np.exp(-0.1 * i) * np.sin(2 * np.pi * x[i])
            
        # Rugged landscape with sinusoidal terms of varying frequencies
        for i in range(self.dim):
            f_val += 0.5 * np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Cross-dimensional interactions with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.2 * np.exp(-0.05 * (i + j)) * np.sin(x[i] + x[j]) * np.cos(x[i] - x[j])
                
        # Polynomial terms with increasing degree to create conditioning
        for i in range(self.dim):
            f_val += 0.1 * x[i]**6 + 0.05 * x[i]**4
            
        # Additional ruggedness through non-linear coupling
        f_val += 0.3 * np.sum(np.sin(0.5 * x)**2)
        
        return f_val