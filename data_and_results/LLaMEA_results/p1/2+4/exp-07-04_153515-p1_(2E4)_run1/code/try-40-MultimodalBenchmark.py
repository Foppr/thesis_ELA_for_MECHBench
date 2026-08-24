import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f_val = np.sum(x**2)
        
        # Enhanced trigonometric components with higher frequencies
        for i in range(self.dim):
            f_val += 0.3 * np.sin(7 * x[i]) * np.cos(4 * x[i]) + 0.2 * np.sin(3 * x[i])**2
        
        # Modified exponential interactions with stronger coupling
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                f_val += 0.1 * np.exp(-0.3 * (x[i] - x[j])**2) * np.sin(5 * (x[i] + x[j]))
        
        # Modified polynomial terms with different exponents
        for i in range(self.dim):
            f_val += 0.03 * (x[i]**6) * np.cos(3 * x[i]) + 0.04 * (x[i]**4) * np.sin(2 * x[i])
        
        # Additional shifted sinusoidal components with different scales
        for i in range(self.dim):
            f_val += 0.2 * np.exp(-0.2 * (x[i] - 1.5)**2) * np.sin(8 * (x[i] + 0.5))
        
        # Global scaling factor with modified sinusoidal influence
        f_val += 0.02 * np.sum(np.abs(x)) * np.sin(0.7 * np.sum(x**2))
        
        # Add cross-terms with higher-order interactions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):
                f_val += 0.05 * (x[i]**2) * (x[j]**3) * np.cos(2 * (x[i] - x[j]))
        
        return f_val