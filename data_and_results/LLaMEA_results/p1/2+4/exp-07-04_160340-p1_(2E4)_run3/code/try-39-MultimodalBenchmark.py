import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply chaotic sinusoidal perturbations
        chaotic_factor = 0.1 * np.sin(10.0 * x) * np.cos(5.0 * x)
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x)))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        
        # Add chaotic perturbations to create complex landscape
        chaotic_term = np.sum(chaotic_factor**2)
        
        # Add multiple global minima at different locations with varying depths
        minima_locations = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying weights
        penalty = 0
        weights = [0.8, 0.6, 0.4, 0.3, 0.5, 0.7]
        for i, (loc, weight) in enumerate(zip(minima_locations, weights)):
            dist = np.sum((shifted_x - loc)**2)
            penalty += weight * np.exp(-dist / (2.0 * (i + 1)))
        
        # Combine all terms with additional interaction terms
        interaction = 0.05 * np.sum(np.sin(shifted_x) * np.cos(shifted_x))
        
        # Final function value
        result = term1 + term2 + term3 + chaotic_term + interaction - penalty
        
        return result