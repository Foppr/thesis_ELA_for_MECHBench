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
                result += 0.8 * (x[i] - 1.2)**2
            else:
                result += 1.2 * (x[i] + 1.2)**2
            
            # Additional terms to create multimodality
            if i < self.dim - 1:
                result += 0.5 * (x[i]**2 + x[i+1]**2) * np.sin(0.8 * (x[i] + x[i+1]))
            
            # Add sinusoidal perturbations to create more complex landscape
            result += 0.3 * np.sin(4.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.2 * x[i]**2)
            
            # Add higher-order polynomial terms for increased complexity
            result += 0.07 * x[i]**4 + 0.02 * x[i]**6
        
        # Add coupling between variables to increase interdependence
        for i in range(0, self.dim - 2, 2):
            result += 0.2 * (x[i] * x[i+1] * x[i+2])**2
        
        # Add a small noise term to make it non-convex
        result += 0.008 * np.sum(np.abs(x)**3)
        
        return result