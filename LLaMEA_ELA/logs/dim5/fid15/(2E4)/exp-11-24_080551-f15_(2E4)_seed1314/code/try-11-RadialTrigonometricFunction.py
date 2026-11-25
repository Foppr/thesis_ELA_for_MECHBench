import numpy as np

class RadialTrigonometricFunction:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Base polynomial term
        result = np.sum(x**4) / 4.0
        
        # Trigonometric components with varying frequencies
        for i in range(self.dim):
            result += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
            
        # Radial basis function components
        center = np.ones(self.dim) * 2.0
        for i in range(self.dim):
            # Radial term with exponential decay
            r = np.sqrt(np.sum((x - center)**2))
            result += 0.5 * np.exp(-0.1 * r**2) * np.sin(2.0 * np.pi * r)
            
        # Cross-dimensional interaction terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Interaction with distance-dependent weight
                dist = np.abs(x[i] - x[j])
                result += 0.3 * np.sin(dist) * np.cos(0.5 * dist)
                
        # Additional global minimum attraction term
        result += 0.1 * np.sum((x - 1.0)**2)
        
        return result