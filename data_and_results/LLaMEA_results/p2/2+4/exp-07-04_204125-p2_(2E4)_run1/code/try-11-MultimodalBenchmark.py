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
            # Main quadratic term with exponential scaling
            result += np.exp(0.5 * abs(x[i])) * (x[i] - 1.0)**2
            
            # Additional terms to create multimodality with asymmetric scaling
            if i < self.dim - 1:
                result += 0.3 * np.exp(0.1 * abs(x[i])) * (x[i] + x[i+1])**2 * np.sin(2 * x[i])
            
            # Add highly oscillatory sinusoidal perturbations with varying frequencies
            result += 0.2 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * x[i]**2)
            
            # Add exponential decay terms to create complex landscape
            result += 0.1 * np.exp(-0.5 * (x[i] - 2.0)**2) * np.sin(3 * x[i])
        
        # Add a high-dimensional coupling term to increase conditioning
        coupling = 0.0
        for i in range(0, self.dim - 2, 2):
            coupling += (x[i] - x[i+1])**4 + 0.5 * (x[i+1] - x[i+2])**3
        result += 0.05 * coupling
        
        # Add a small noise term to make it non-convex
        result += 0.005 * np.sum(x**6)
        
        return result