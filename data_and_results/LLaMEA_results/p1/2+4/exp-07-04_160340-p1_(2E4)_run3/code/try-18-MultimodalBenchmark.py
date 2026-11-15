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
        chaotic_factor = 0.1 * np.sum(np.sin(np.pi * x) * np.cos(np.pi * x))
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(x)))**2)
        term3 = 0.1 * np.sum(x**4)
        
        # Add chaotic perturbation to the landscape
        chaotic_perturbation = 0.5 * np.sin(10 * np.sum(x**2)) * np.cos(5 * np.sum(x**2))
        
        # Create multiple nested global minima with varying depths
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
        weights = [1.0, 0.8, 0.6, 0.4, 0.3, 0.2]
        for i, loc in enumerate(minima_locations):
            dist = np.sum((x - loc)**2)
            penalty += weights[i] * np.exp(-dist / 5.0)
        
        # Combine all terms with chaotic influence
        result = term1 + term2 + term3 + chaotic_factor + chaotic_perturbation - penalty
        
        return result