import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Main quadratic term
        f_val = np.sum(x**2)
        
        # Add exponentially increasing complexity local minima
        for i in range(self.dim):
            f_val += 0.5 * np.exp(-0.1 * np.abs(x[i])) * np.sin(10 * x[i]) * np.cos(7 * x[i])
            
        # Add high-frequency oscillations
        for i in range(self.dim):
            f_val += 0.3 * np.sin(20 * x[i]) * np.cos(15 * x[i]) * np.sin(5 * x[i])
            
        # Add coupled multi-dimensional local optima
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for complexity control
                f_val += 0.2 * np.sin(3 * x[i]) * np.cos(4 * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
                
        # Add a global scaling factor that increases with dimensionality
        f_val *= (1.0 + 0.1 * self.dim)
        
        return f_val