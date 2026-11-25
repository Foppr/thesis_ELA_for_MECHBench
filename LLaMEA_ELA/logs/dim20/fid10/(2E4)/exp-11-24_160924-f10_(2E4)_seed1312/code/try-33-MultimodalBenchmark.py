import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add polynomial and sinusoidal components with varying frequencies
        for i in range(self.dim):
            xi = x[i]
            # Combine polynomial and sinusoidal terms to create complex landscape
            result += (xi**6 - 15 * xi**4 + 75 * xi**2 - 125) * np.sin(0.3 * xi) + 0.7 * xi**4 * np.cos(0.7 * xi)
            
        # Add cross-dimensional coupling with non-separable interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+5, self.dim)):  # Increased coupling for more complexity
                # Introduce highly non-linear dependencies between dimensions
                result += 0.5 * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(3 * (x[i] + x[j]))
                
        # Add a global scaling term to increase conditioning difficulty
        result += 0.02 * np.sum(x**8) + 0.03 * np.sum(np.cos(4 * x)) + 0.01 * np.sum(np.sin(2 * x))
        
        # Add a complex interaction term that creates multiple local minima
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.4 * np.sin(5 * (x[i]**2 + x[j]**2)) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        return result