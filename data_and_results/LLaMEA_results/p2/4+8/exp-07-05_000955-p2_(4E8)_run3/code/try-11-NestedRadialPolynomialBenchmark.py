import numpy as np

class NestedRadialPolynomialBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': -5.0, 'ub': 5.0})()
    
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial basis function component with multiple centers
        result = 0.0
        centers = np.linspace(-0.8, 0.8, min(5, self.dim))
        for i in range(min(5, self.dim)):
            center = centers[i] * np.ones(self.dim)
            distance = np.sum((x_norm - center) ** 2)
            result += np.exp(-5 * distance) * np.cos(2 * np.pi * distance)
        
        # Add polynomial penalty terms with varying degrees
        for i in range(self.dim):
            result += 0.1 * (x_norm[i] ** 4) + 0.05 * (x_norm[i] ** 3) + 0.2 * (x_norm[i] ** 2)
        
        # Add interaction terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * x_norm[i] * x_norm[j] * np.sin(3 * np.pi * x_norm[i])
        
        # Global scaling and offset
        result = result * 2.0 + 0.5 * np.sum(x_norm ** 2)
        
        return result