import numpy as np

class ChaoticMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Add chaotic exponential components
        for i in range(self.dim):
            xi = x[i]
            result += np.exp(0.1 * xi**2) * np.sin(5 * xi) + 0.5 * np.cos(3 * xi)
            
        # Add cross-dimensional coupling with chaotic interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Introduce chaotic coupling between dimensions
                coupling = np.sin(x[i] * x[j]) * np.exp(-0.1 * (x[i] - x[j])**2)
                result += 0.3 * coupling
                
        # Add a saddle-point structure with mixed quadratic and quartic terms
        for i in range(self.dim):
            xi = x[i]
            result += 0.1 * xi**4 - 0.5 * xi**2 + 0.05 * np.sin(10 * xi)
            
        # Add a global forcing term with irregular oscillations
        result += 0.2 * np.sum(np.exp(-0.05 * x**2) * np.cos(2 * np.pi * x))
        
        return result