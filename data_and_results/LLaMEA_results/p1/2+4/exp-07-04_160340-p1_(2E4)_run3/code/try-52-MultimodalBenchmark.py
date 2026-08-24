import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply enhanced chaotic perturbation using a modified logistic map
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= (4.0 * ((x[i] / 5.0) + 0.1) * (1.0 - (x[i] / 5.0) - 0.1))
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x) + 1e-8))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        
        # Add enhanced chaotic sinusoidal perturbations
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += np.sin(17 * np.pi * x[i]) * np.cos(9 * np.pi * x[i]) + 0.6 * np.sin(27 * np.pi * x[i])
        
        # Add multiple global minima at different locations with varying depths
        minima_locations = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim),
            np.array([1.5] * self.dim),
            np.array([-1.5] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying weights
        penalty = 0
        weights = [0.5, 0.3, 0.7, 0.4, 0.6, 0.8, 0.9, 0.2]
        for i, (loc, weight) in enumerate(zip(minima_locations, weights)):
            distance = np.sum((shifted_x - loc)**2)
            penalty += weight * np.exp(-distance / (2.0 * (i + 1)**2))
        
        # Combine all terms with chaotic influence
        result = term1 + term2 + term3 + chaotic_perturbation - penalty
        
        # Add a more complex nested structure with multiple local optima
        nested_term = 0.06 * np.sum(np.sin(32 * x)**2) + 0.04 * np.sum(np.cos(17 * x)**2)
        result += nested_term
        
        # Add a noise component to increase difficulty
        noise = 0.015 * np.sum(np.random.randn(self.dim) * x)
        result += noise
        
        return result