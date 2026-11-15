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
        chaotic_factor = 0.1 * np.sin(10 * x) * np.cos(5 * x)
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(x)))**2)
        term3 = 0.1 * np.sum(x**4)
        
        # Add chaotic perturbations to create complex landscape
        perturbed_x = x + chaotic_factor
        
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
        weights = [1.0, 0.8, 1.2, 0.6, 0.9, 1.1]
        for i, (loc, weight) in enumerate(zip(minima_locations, weights)):
            distance = np.sum((perturbed_x - loc)**2)
            penalty += weight * np.exp(-distance / 5.0)
        
        # Add nested structure with additional sinusoidal modulation
        nested_term = 0.05 * np.sum(np.sin(3 * x) * np.cos(2 * x))
        
        # Combine all terms
        result = term1 + term2 + term3 + nested_term - penalty
        
        return result