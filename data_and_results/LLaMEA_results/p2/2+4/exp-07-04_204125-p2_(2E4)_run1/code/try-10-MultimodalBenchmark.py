import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Add multiple quadratic terms with different scales and offsets
        for i in range(self.dim):
            # Main quadratic term with asymmetric scaling
            if i % 2 == 0:
                result += 0.7 * (x[i] - 1.0)**2
            else:
                result += 1.3 * (x[i] + 1.0)**2
            
            # Additional terms to create multimodality
            if i < self.dim - 1:
                result += 0.4 * (x[i]**2 + x[i+1]**2) * np.sin(0.7 * (x[i] + x[i+1]))
            
            # Add sinusoidal perturbations to create more complex landscape
            result += 0.25 * np.sin(3.5 * x[i]) * np.cos(1.5 * x[i]) * np.exp(-0.15 * x[i]**2)
            
            # Add higher-order polynomial terms for increased complexity
            result += 0.06 * x[i]**4 + 0.015 * x[i]**6
        
        # Add coupling between variables to increase interdependence
        for i in range(0, self.dim - 2, 2):
            result += 0.15 * (x[i] * x[i+1] * x[i+2])**2
        
        # Add a small noise term to make it non-convex
        result += 0.007 * np.sum(np.abs(x)**3)
        
        return result