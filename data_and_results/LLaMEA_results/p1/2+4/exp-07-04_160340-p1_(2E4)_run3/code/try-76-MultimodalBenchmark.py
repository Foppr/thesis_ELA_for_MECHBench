import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply enhanced chaotic perturbation using sine-based map
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= np.sin(10 * np.pi * (x[i] / 5.0))**2
        
        # Shift variables to center the function
        shifted_x = x
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x)))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        
        # Add enhanced chaotic sinusoidal perturbations
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += np.sin(15 * np.pi * x[i]) * np.cos(7 * np.pi * x[i])
        
        # Add multiple global minima at different locations with varying depths
        minima_locations = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim),
            np.array([0.0] * self.dim),
            np.array([3.0] * self.dim),
            np.array([-3.0] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying weights
        penalty = 0
        weights = [0.5, 0.3, 0.7, 0.4, 0.6, 0.8, 0.9, 0.2, 0.1]
        for i, (loc, weight) in enumerate(zip(minima_locations, weights)):
            distance = np.sum((shifted_x - loc)**2)
            penalty += weight * np.exp(-distance / (2.0 * (i + 1)**2))
        
        # Combine all terms with chaotic influence
        result = term1 + term2 + term3 + chaotic_perturbation - penalty
        
        # Add a complex nested structure with multiple local optima and enhanced nonlinearity
        nested_term = 0.05 * np.sum(np.sin(25 * x)**2 + 0.1 * np.sin(50 * x)**4)
        result += nested_term
        
        # Add a new chaotic component that increases complexity
        chaotic_component = 0.02 * np.sum(np.sin(30 * x) * np.cos(15 * x))
        result += chaotic_component
        
        return result