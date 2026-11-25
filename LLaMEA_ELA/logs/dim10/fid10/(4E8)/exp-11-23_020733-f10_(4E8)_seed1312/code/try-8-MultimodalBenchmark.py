import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Scale input to [-5, 5] if not already in that range
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize function value
        f_val = 0.0
        
        # Add exponential decay terms with sinusoidal modulation
        for i in range(self.dim):
            f_val += np.exp(-0.1 * np.abs(x[i])) * np.sin(2 * np.pi * x[i])
        
        # Add trigonometric wave interactions between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.5 * np.cos(0.5 * (x[i] + x[j])) * np.sin(0.3 * (x[i] - x[j]))
        
        # Add polynomial penalty terms
        for i in range(self.dim):
            f_val += 0.01 * (x[i]**6 - 2*x[i]**4 + x[i]**2)
        
        # Add global shaping term with multiple local minima
        f_val += 0.1 * np.sum(np.sin(0.2 * x) ** 2)
        
        # Add steep gradient regions near boundaries
        boundary_penalty = 0.0
        for i in range(self.dim):
            if np.abs(x[i]) > 4.5:
                boundary_penalty += 10 * (np.abs(x[i]) - 4.5)**2
        f_val += boundary_penalty
        
        return f_val