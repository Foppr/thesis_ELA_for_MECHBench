import numpy as np

class SinusoidalOptimizationLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with quadratic base
        result = np.sum(x**2) * 0.5
        
        # Add multi-frequency sinusoidal components for local optima
        for i in range(self.dim):
            result += 0.2 * np.sin(3 * x[i]) * np.cos(7 * x[i]) + \
                     0.1 * np.sin(2 * x[i]) * np.cos(5 * x[i])
            
        # Add higher-order interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i] * x[j]) * np.cos(x[i]**2 + x[j]**2) + \
                         0.05 * np.sin(x[i] + x[j])**2 * np.cos(x[i] - x[j])**2
                
        # Add cross-dimensional coupling with exponential decay
        for i in range(self.dim):
            result += 0.08 * np.exp(-0.1 * np.sum((x - x[i])**2)) * np.sin(4 * x[i])
            
        # Add a small noise term to make it non-trivial
        result += 0.005 * np.random.random()
        
        return result