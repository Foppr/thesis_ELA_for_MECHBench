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
            result += (xi**6 - 10 * xi**4 + 35 * xi**2 - 30) * np.sin(0.7 * xi) + 0.3 * xi**5 * np.cos(1.3 * xi)
            
        # Add cross-dimensional coupling with non-separable interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+6, self.dim)):  # Extended coupling for increased complexity
                # Introduce highly non-linear dependencies between dimensions
                result += 0.5 * np.exp(-0.2 * (x[i] - x[j])**2) * np.sin(3 * (x[i] + x[j]))
                
        # Add a global scaling term to increase conditioning difficulty
        result += 0.02 * np.sum(x**8) + 0.03 * np.sum(np.cos(5 * x)) + 0.01 * np.sum(np.sin(2 * x))
        
        # Add a highly non-separable interaction term involving all dimensions
        result += 0.4 * np.exp(-0.1 * np.sum((x - np.mean(x))**2)) * np.cos(0.5 * np.sum(x**3))
        
        return result