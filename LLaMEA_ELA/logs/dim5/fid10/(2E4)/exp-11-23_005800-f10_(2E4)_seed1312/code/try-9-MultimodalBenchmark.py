import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Base quadratic term
        f_val = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal perturbations
        for i in range(self.dim):
            f_val += 0.1 * np.sin(5 * np.pi * x_normalized[i]) * np.cos(3 * np.pi * x_normalized[i])
            
        # Add cross-terms to increase complexity
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.05 * np.sin(2 * np.pi * (x_normalized[i] + x_normalized[j]))
                
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.01 * np.sum(np.abs(x_normalized)**3)
        
        return f_val