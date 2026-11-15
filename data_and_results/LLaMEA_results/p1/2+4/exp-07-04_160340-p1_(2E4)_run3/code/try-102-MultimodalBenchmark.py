import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply enhanced chaotic perturbation using logistic map with multiple iterations
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= (4.0 * (x[i] / 5.0) * (1.0 - (x[i] / 5.0)))
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Calculate multiple sinusoidal components with varying frequencies and amplitudes
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x)))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        
        # Add enhanced chaotic sinusoidal perturbations with multiple frequencies
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += np.sin(15 * np.pi * x[i]) * np.cos(7 * np.pi * x[i]) + \
                                   np.sin(8 * np.pi * x[i]) * np.cos(3 * np.pi * x[i])
        
        # Add multiple global minima at different locations with varying depths and dynamic weights
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
        
        # Add multiple nested structures with varying complexity
        nested_term = 0.05 * np.sum(np.sin(20 * x)**2) + \
                      0.03 * np.sum(np.sin(30 * x)**3) + \
                      0.02 * np.sum(np.cos(25 * x)**2)
        result += nested_term
        
        # Add a dynamic scaling factor based on the chaotic influence
        dynamic_scale = 1.0 + 0.1 * np.abs(chaotic_factor)
        result *= dynamic_scale
        
        return result