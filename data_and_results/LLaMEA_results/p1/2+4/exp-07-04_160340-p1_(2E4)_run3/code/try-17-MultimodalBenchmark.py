import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply chaotic perturbation using logistic map
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= (4.0 * (x[i] / 5.0) * (1.0 - (x[i] / 5.0)))
        
        # Shift variables to center the function
        shifted_x = x / 2.0
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(shifted_x * np.pi)**2)
        term3 = np.sum(np.sin(shifted_x * np.pi * 2)**2)
        term4 = 0.1 * np.sum(shifted_x**4)
        
        # Add chaotic sinusoidal perturbations
        chaotic_perturbation = 0.5 * np.sum(np.sin(shifted_x * np.pi * 3) * np.sin(shifted_x * np.pi * 5))
        
        # Add multiple nested global minima at different scales
        minima_locations = [
            np.array([0.0] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim),
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying weights
        penalty = 0
        weights = [1.0, 0.8, 0.8, 0.6, 0.6, 0.4, 0.4]
        for i, (loc, weight) in enumerate(zip(minima_locations, weights)):
            distance = np.sum((shifted_x - loc)**2)
            penalty += weight * np.exp(-distance / 5.0)
        
        # Combine all terms with chaotic modulation
        result = (term1 + term2 + term3 + term4 + chaotic_perturbation - penalty) * chaotic_factor
        
        return result