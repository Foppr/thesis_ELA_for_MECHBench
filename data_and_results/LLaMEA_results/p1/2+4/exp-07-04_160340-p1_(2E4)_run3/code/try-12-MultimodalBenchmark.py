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
        shifted_x = x
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(5.0 * np.sqrt(np.abs(shifted_x)))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        term4 = 0.05 * np.sum(np.sin(3.0 * shifted_x)**2)
        
        # Add multiple global minima at different locations with varying weights
        minima_locations = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying strengths
        penalty = 0
        for i, loc in enumerate(minima_locations):
            # Varying penalty strengths for different minima
            strength = 0.3 + 0.2 * (i % 3)
            penalty += strength * np.exp(-np.sum((shifted_x - loc)**2) / 5.0)
        
        # Add a complex saddle point structure
        saddle_term = 0.2 * np.sum(np.sin(shifted_x / 2.0) * np.cos(shifted_x / 3.0))
        
        # Combine all terms
        result = term1 + term2 + term3 + term4 + saddle_term - penalty
        
        return result