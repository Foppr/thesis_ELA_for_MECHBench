import numpy as np

class HybridMultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Initialize result
        result = 0.0
        
        # Polynomial terms with varying degrees
        for i in range(self.dim):
            result += 0.5 * x[i]**4 - 2.0 * x[i]**3 + 1.5 * x[i]**2
            
        # Sinusoidal coupling between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited coupling
                result += 0.3 * np.sin(3 * np.pi * x[i]) * np.cos(2 * np.pi * x[j])
                
        # Radial basis function component
        center = np.ones(self.dim) * 2.0
        for i in range(self.dim):
            result += 0.2 * np.exp(-0.1 * (x[i] - center[i])**2)
            
        # Additional high-frequency oscillation
        for i in range(self.dim):
            result += 0.1 * np.sin(10 * x[i]) * np.cos(5 * x[i])
            
        # Add a global minimum at origin with penalty
        result += 0.05 * np.sum(x**2)
        
        return result