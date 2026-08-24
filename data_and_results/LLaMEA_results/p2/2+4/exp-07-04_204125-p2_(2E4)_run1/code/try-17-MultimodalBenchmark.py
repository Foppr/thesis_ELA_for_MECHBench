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
            # Main quadratic term with adaptive scaling
            result += (x[i] - 1.0)**2 * (1.0 + 0.1 * np.abs(x[i]))
            
            # Additional coupling terms to create multimodality
            if i < self.dim - 1:
                result += 0.3 * (x[i]**2 + x[i+1]**2) * np.sin(0.5 * (x[i] + x[i+1]))
            
            # Add higher-order polynomial perturbations for increased complexity
            result += 0.05 * x[i]**4 + 0.02 * x[i]**6
            
            # Add coupled sinusoidal perturbations with varying frequencies
            result += 0.15 * np.sin(3 * x[i]) * np.cos(2 * x[i]) * np.exp(-0.1 * np.abs(x[i]))
            
            # Add cross-terms between variables to increase interdependence
            if i < self.dim - 2:
                result += 0.08 * x[i] * x[i+1] * x[i+2]
        
        # Add a small noise term to make it non-convex
        result += 0.005 * np.sum(x**8)
        
        return result