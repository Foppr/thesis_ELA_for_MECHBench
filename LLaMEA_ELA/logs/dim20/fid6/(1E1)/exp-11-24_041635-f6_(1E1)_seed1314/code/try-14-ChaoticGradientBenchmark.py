import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Chaotic sine-wave interactions with adaptive scaling
        for i in range(self.dim):
            xi = x[i]
            # Adaptive frequency based on dimension
            freq = 2.0 + 0.5 * np.sin(i / (self.dim + 1))
            
            # Multiple chaotic components
            result += (
                0.5 * xi**2 +
                2.0 * np.sin(freq * xi) * np.cos(3.0 * xi) +
                0.8 * np.sin(7.0 * xi)**2 +
                1.2 * np.exp(-0.1 * xi**2) * np.sin(5.0 * xi) +
                0.3 * np.cos(4.0 * xi) * np.exp(-0.05 * xi**2) +
                0.6 * np.sin(2.0 * xi)**3 * np.cos(xi) +
                0.4 * np.exp(-0.2 * np.abs(xi)) * np.sin(6.0 * xi)
            )
            
            # Cross-dimensional coupling with chaotic interaction
            for j in range(i+1, self.dim):
                xj = x[j]
                coupling = np.sin(2.5 * (xi + xj)) * np.cos(1.5 * (xi - xj))
                result += 0.1 * coupling * (1.0 + 0.1 * (i + j))
        
        # Add dimension-dependent complexity
        result += 0.01 * np.sum(x**8) + 0.02 * np.sum(np.abs(x)**3)
        
        return result