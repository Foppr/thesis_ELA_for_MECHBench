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
            chaotic_factor *= (3.8 * (x[i] / 5.0) * (1.0 - (x[i] / 5.0)) + 0.1 * np.sin(2 * np.pi * x[i] / 5.0))
        
        # Shift variables to center the function
        shifted_x = x - 0.5
        
        # Calculate multiple sinusoidal components with varying frequencies and amplitudes
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x)))**3)
        term3 = 0.15 * np.sum(shifted_x**4)
        
        # Add enhanced chaotic sinusoidal perturbations
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += np.sin(15 * np.pi * x[i]) * np.cos(7 * np.pi * x[i]) * np.exp(-0.1 * np.abs(x[i]))
        
        # Add multiple global minima at different locations with varying depths and complexities
        minima_locations = [
            np.array([0.8] * self.dim),
            np.array([-0.8] * self.dim),
            np.array([1.2] * self.dim),
            np.array([-1.2] * self.dim),
            np.array([0.0] * self.dim),
            np.array([2.5] * self.dim),
            np.array([-2.5] * self.dim),
            np.array([1.5] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying weights and exponents
        penalty = 0
        weights = [0.6, 0.4, 0.8, 0.5, 0.7, 0.9, 0.3, 0.55]
        exponents = [2, 3, 2, 4, 3, 2, 5, 3]
        for i, (loc, weight, exp) in enumerate(zip(minima_locations, weights, exponents)):
            distance = np.sum((shifted_x - loc)**2)
            penalty += weight * np.exp(-distance / (2.0 * (i + 1)**exp))
        
        # Combine all terms with enhanced chaotic influence
        result = term1 + term2 + term3 + chaotic_perturbation - penalty
        
        # Add a more complex nested structure with multiple local optima and fractal-like features
        nested_term = 0.08 * np.sum(np.sin(30 * x)**2 + 0.5 * np.sin(60 * x)**2)
        result += nested_term
        
        # Add a final chaotic modulation to increase landscape complexity
        final_modulation = 0.05 * np.sum(np.sin(50 * x) * np.cos(25 * x))
        result += final_modulation
        
        return result