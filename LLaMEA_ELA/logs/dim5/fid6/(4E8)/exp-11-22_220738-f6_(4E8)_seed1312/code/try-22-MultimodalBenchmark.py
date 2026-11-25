import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        f_val = np.sum(x**2)
        
        # Add exponential decay terms with trigonometric modulation
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.1 * np.abs(x[i])) * np.sin(10 * x[i])
            
        # Add high-frequency oscillations to increase complexity
        for i in range(self.dim):
            f_val += 0.3 * np.sin(20 * x[i]) * np.cos(15 * x[i])
            
        # Add interaction terms between dimensions
        if self.dim >= 2:
            for i in range(self.dim - 1):
                f_val += 0.2 * np.exp(-0.05 * (x[i]**2 + x[i+1]**2)) * np.sin(5 * (x[i] - x[i+1]))
                
        return f_val