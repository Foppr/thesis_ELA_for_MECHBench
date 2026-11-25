import numpy as np

class ComplexMultimodalFunction:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        result = 0.0
        
        # Polynomial base with varying degrees
        for i in range(self.dim):
            xi = x[i]
            result += (xi ** 4) * (1 + 0.3 * np.sin(5 * xi))
            
        # Add trigonometric modulation with multiple frequencies
        for i in range(self.dim):
            xi = x[i]
            result += 3 * np.sin(2 * xi) * np.cos(3 * xi) * np.exp(-0.1 * abs(xi))
            
        # Interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, min(i+4, self.dim)):  # Limited interaction
                result += 0.5 * np.sin(x[i] * x[j]) * (1 + 0.2 * np.cos(2 * (x[i] + x[j])))
                
        # Exponential penalty for large values
        result += 2 * np.exp(0.05 * np.sum(np.abs(x)))
        
        # Add a global shift to make the function more challenging
        shift = 1.0
        result += shift * np.sum(np.sin(x) * np.cos(x))
        
        return result