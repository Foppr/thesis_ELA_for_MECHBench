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
            result += (xi**4 - 8 * xi**2 + 16) * np.sin(0.5 * xi) + 0.5 * xi**3 * np.cos(xi)
            
        # Add cross-dimensional coupling with non-separable interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling for scalability
                # Introduce highly non-linear dependencies between dimensions
                result += 0.3 * np.sin(2 * (x[i] + x[j])) * np.exp(-0.1 * (x[i] - x[j])**2)
                
        # Add a global scaling term to increase conditioning difficulty
        result += 0.01 * np.sum(x**6) + 0.02 * np.sum(np.cos(3 * x))
        
        return result