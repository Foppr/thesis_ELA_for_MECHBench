import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal perturbations
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.1 * np.abs(x[i])) * np.sin(10 * x[i])
            
        # Add a complex global minimum structure with polynomial interactions
        f_val += 0.3 * np.sum((x - 1.0)**4) * np.cos(3 * np.sum(x))
        
        # Introduce a high-dimensional saddle point structure
        f_val += 0.2 * np.sum(np.sin(x) * np.cos(x)**2)
        
        # Add a chaotic component with varying frequency
        f_val += 0.1 * np.sum(np.sin(20 * x + np.sin(15 * x)))
        
        return f_val