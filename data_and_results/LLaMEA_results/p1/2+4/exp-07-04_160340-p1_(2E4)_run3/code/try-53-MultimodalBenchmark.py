import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply enhanced chaotic perturbation using a modified logistic map with higher chaos
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= (4.0 * ((x[i] / 5.0) + 0.05) * (1.0 - (x[i] / 5.0) - 0.05))
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x)))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        
        # Add enhanced chaotic sinusoidal perturbations with higher frequency components
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += (np.sin(20 * np.pi * x[i]) * np.cos(10 * np.pi * x[i]) + 
                                   0.5 * np.sin(30 * np.pi * x[i]) + 
                                   0.3 * np.cos(25 * np.pi * x[i]))
        
        # Add multiple global minima at different locations with varying depths and more complex weights
        minima_locations = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim),
            np.array([1.5] * self.dim),
            np.array([-1.5] * self.dim),
            np.array([0.0] * self.dim),
            np.array([3.0] * self.dim),
            np.array([-3.0] * self.dim),
            np.array([0.75] * self.dim),
            np.array([-0.75] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying weights
        penalty = 0
        weights = [0.5, 0.3, 0.7, 0.4, 0.6, 0.8, 0.9, 0.2, 0.1, 0.45, 0.55, 0.35, 0.65]
        for i, (loc, weight) in enumerate(zip(minima_locations, weights)):
            distance = np.sum((shifted_x - loc)**2)
            penalty += weight * np.exp(-distance / (2.0 * (i + 1)**2))
        
        # Combine all terms with chaotic influence
        result = term1 + term2 + term3 + chaotic_perturbation - penalty
        
        # Add a more complex nested structure with multiple local optima and increased difficulty
        nested_term = 0.05 * np.sum(np.sin(40 * x)**2) + 0.03 * np.sum(np.cos(20 * x)**2) + 0.02 * np.sum(np.sin(50 * x)**3)
        result += nested_term
        
        # Add a noise component to increase difficulty with higher variance
        noise = 0.02 * np.sum(np.random.randn(self.dim) * x)
        result += noise
        
        # Add a complex interaction term between dimensions to increase coupling
        interaction_term = 0.01 * np.sum(np.sin(x[:-1] - x[1:]) * np.cos(x[:-1] + x[1:]))
        result += interaction_term
        
        return result