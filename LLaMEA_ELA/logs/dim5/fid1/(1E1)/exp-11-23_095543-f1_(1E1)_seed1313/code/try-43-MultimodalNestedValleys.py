import numpy as np

class MultimodalNestedValleys:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Global minimum at origin
        if np.allclose(x, 0):
            return 0.0
            
        # Quadratic base with varying condition numbers
        result = 0.0
        for i in range(self.dim):
            result += (10 ** (2 * i / (self.dim - 1))) * (x[i] ** 2)
            
        # Add trigonometric modulations to create valleys and ridges
        for i in range(self.dim):
            result += 0.5 * np.sin(3 * x[i]) * np.cos(5 * x[(i + 1) % self.dim])
            
        # Radial basis function components with multiple peaks
        for i in range(self.dim):
            r = np.sqrt(np.sum(x ** 2))
            result += 0.3 * np.exp(-0.5 * (x[i] - r) ** 2) * np.sin(2 * np.pi * r)
            
        # Add coupling terms between dimensions to create complex interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling = np.exp(-0.05 * (x[i] ** 2 + x[j] ** 2))
                result += coupling * np.sin(3 * x[i]) * np.cos(4 * x[j])
                
        # Add a quartic polynomial to increase local complexity
        for i in range(self.dim):
            result += 0.1 * (x[i] ** 4) * np.cos(2 * x[i])
            
        # Add a radial component that creates nested structures
        r = np.sqrt(np.sum(x ** 2))
        result += 0.2 * np.sin(10 * r) * np.exp(-0.1 * r)
        
        # Normalize to prevent extreme values
        result /= (1.0 + 0.05 * np.sum(x ** 2))
        
        return result