import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add separable polynomial and exponential components
        for i in range(self.dim):
            xi = x[i]
            # Combine polynomial and exponential terms with varying exponents
            result += (xi**6 - 10 * xi**4 + 35 * xi**2 - 50) * np.exp(-0.1 * xi**2) + 0.1 * xi**5 * np.sin(xi)
            
        # Add cross-dimensional coupling with separable interaction terms
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited coupling for scalability
                # Introduce separable but non-linear dependencies between dimensions
                result += 0.2 * (x[i]**2 + x[j]**2) * np.exp(-0.05 * (x[i] - x[j])**2)
                
        # Add a global conditioning term to increase difficulty
        result += 0.005 * np.sum(x**8) + 0.01 * np.sum(np.sin(2 * x)**2)
        
        return result