import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already in that range
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add polynomial terms
        for i in range(self.dim):
            f_val += x[i]**4 - 16*x[i]**2 + 5*x[i]
        
        # Add sinusoidal oscillations
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += np.sin(x[i]) * np.cos(x[j])
        
        # Add interaction terms
        for i in range(self.dim):
            f_val += 0.1 * x[i]**3 * np.sin(0.5 * x[i])
        
        # Add global minimum at origin with additional penalty
        f_val += 0.01 * np.sum(x**2)
        
        return f_val