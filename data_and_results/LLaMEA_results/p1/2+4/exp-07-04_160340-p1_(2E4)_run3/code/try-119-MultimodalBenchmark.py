import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply enhanced chaotic perturbation using logistic map with higher growth rate
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= (4.5 * (x[i] / 5.0) * (1.0 - (x[i] / 5.0)))
        
        # Shift variables to center the function
        shifted_x = x - 0.5
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x)))**3)
        term3 = 0.15 * np.sum(shifted_x**4)
        
        # Add enhanced chaotic sinusoidal perturbations with higher frequencies
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += np.sin(15 * np.pi * x[i]) * np.cos(8 * np.pi * x[i])
        
        # Add multiple global minima at different locations with varying depths
        minima_locations = [
            np.array([1.5] * self.dim),
            np.array([-1.5] * self.dim),
            np.array([0.7] * self.dim),
            np.array([-0.7] * self.dim),
            np.array([2.5] * self.dim),
            np.array([-2.5] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with adjusted weights
        penalty = 0
        weights = [0.7, 0.5, 0.8, 0.6, 0.9, 0.4]
        for i, (loc, weight) in enumerate(zip(minima_locations, weights)):
            distance = np.sum((shifted_x - loc)**2)
            penalty += weight * np.exp(-distance / (2.0 * (i + 1)**3))
        
        # Combine all terms with chaotic influence
        result = term1 + term2 + term3 + chaotic_perturbation - penalty
        
        # Add enhanced nested structure with multiple local optima
        nested_term = 0.08 * np.sum(np.sin(25 * x)**2)
        result += nested_term
        
        return result