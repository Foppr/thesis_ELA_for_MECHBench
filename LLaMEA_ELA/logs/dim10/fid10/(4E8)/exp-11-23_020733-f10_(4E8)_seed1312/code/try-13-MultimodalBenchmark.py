import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add polynomial terms with different degrees to create local minima
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 2.0 * x[i]**2
        
        # Add trigonometric terms to increase complexity
        for i in range(self.dim):
            result += 0.3 * np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Add interaction terms between dimensions using exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(x[i] * x[j])
        
        # Add a global oscillation term to increase difficulty
        result += 0.2 * np.exp(-0.1 * np.sum(x**2)) * np.sin(5 * np.sum(x))
        
        return result