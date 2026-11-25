import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_normalized = x / 5.0
        
        # Base quadratic term
        f_val = np.sum(x_normalized**2)
        
        # Add multiple local minima using sinusoidal perturbations with varying frequencies
        for i in range(self.dim):
            f_val += 0.15 * np.sin(7 * np.pi * x_normalized[i]) * np.cos(4 * np.pi * x_normalized[i])
            
        # Add cross-terms to increase complexity with interaction between variables
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.08 * np.sin(3 * np.pi * (x_normalized[i] + x_normalized[j])) * np.cos(2 * np.pi * (x_normalized[i] - x_normalized[j]))
                
        # Add a global minimum at origin with additional penalty terms
        f_val += 0.02 * np.sum(np.abs(x_normalized)**4)
        
        # Add a more complex interaction term for higher dimensional difficulty
        if self.dim > 1:
            f_val += 0.05 * np.sin(6 * np.pi * np.sum(x_normalized**2))
            
        return f_val