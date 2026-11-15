import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Calculate multiple sinusoidal components
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x)))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        
        # Add multiple global minima at different locations
        minima_locations = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty
        penalty = 0
        for loc in minima_locations:
            penalty += 0.5 * np.exp(-np.sum((shifted_x - loc)**2) / 10.0)
        
        # Combine all terms
        result = term1 + term2 + term3 - penalty
        
        return result