import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with adaptive scaling
        f_val = np.sum(x**2) * (1.0 + 0.1 * np.mean(np.abs(x)))
        
        # High-frequency sinusoidal components with exponential decay
        for i in range(self.dim):
            freq = 15.0 * np.exp(-0.1 * i)
            f_val += 0.3 * np.sin(freq * x[i]) * np.cos(7 * x[i]) * np.exp(-0.05 * i)
        
        # Cross-dimensional interaction with exponential decay
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited range for correlation
                decay = np.exp(-0.2 * (j - i))
                f_val += 0.1 * decay * np.sin(x[i]) * np.cos(x[j]) * np.sin(3 * x[i] + 2 * x[j])
        
        # Quartic and sextic penalties with adaptive weights
        f_val += 0.05 * np.sum(np.abs(x)**4) + 0.03 * np.sum(np.abs(x)**6)
        
        # Chaos-inducing term with non-linear transformation
        chaos_term = 0.08 * np.prod(np.sin(2 * x + np.pi/4))
        f_val += chaos_term
        
        # Adaptive basin conditioning
        basin_factor = 1.0 + 0.2 * np.exp(-np.sum(x**2) / (2 * self.dim))
        f_val *= basin_factor
        
        return f_val