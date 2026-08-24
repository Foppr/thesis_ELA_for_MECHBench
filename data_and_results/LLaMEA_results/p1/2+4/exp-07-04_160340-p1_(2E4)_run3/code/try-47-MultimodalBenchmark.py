import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply enhanced chaotic perturbation using a modified logistic map with higher sensitivity
        chaotic_factor = 1.0
        for i in range(self.dim):
            chaotic_factor *= (4.0 * ((x[i] / 5.0) + 0.05) * (1.0 - (x[i] / 5.0) - 0.05))
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Calculate multiple sinusoidal components with varying frequencies and amplitudes
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x)))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        term4 = 0.05 * np.sum(np.cos(2 * shifted_x)**3)
        term5 = 0.03 * np.sum(np.sin(3 * shifted_x)**4)
        
        # Add enhanced chaotic sinusoidal perturbations with higher frequency components
        chaotic_perturbation = 0.0
        for i in range(self.dim):
            chaotic_perturbation += (np.sin(20 * np.pi * x[i]) * np.cos(10 * np.pi * x[i]) + 
                                   0.7 * np.sin(30 * np.pi * x[i]) + 
                                   0.3 * np.cos(25 * np.pi * x[i]) + 
                                   0.5 * np.sin(35 * np.pi * x[i]))
        
        # Add multiple global minima at different locations with varying depths and complex interactions
        minima_locations = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim),
            np.array([1.5] * self.dim),
            np.array([-1.5] * self.dim),
            np.array([0.25] * self.dim),
            np.array([-0.25] * self.dim),
            np.array([2.5] * self.dim),
            np.array([-2.5] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty with varying weights and interaction terms
        penalty = 0
        weights = [0.5, 0.3, 0.7, 0.4, 0.6, 0.8, 0.9, 0.2, 0.1, 0.95, 0.35, 0.65]
        for i, (loc, weight) in enumerate(zip(minima_locations, weights)):
            distance = np.sum((shifted_x - loc)**2)
            penalty += weight * np.exp(-distance / (2.0 * (i + 1)**2)) * (1.0 + 0.1 * np.sin(5 * distance))
        
        # Combine all terms with chaotic influence
        result = term1 + term2 + term3 + term4 + term5 + chaotic_perturbation - penalty
        
        # Add a more complex nested structure with multiple local optima and fractal-like features
        nested_term = 0.05 * np.sum(np.sin(40 * x)**2) + 0.03 * np.sum(np.cos(20 * x)**2) + 0.02 * np.sum(np.sin(50 * x)**3)
        result += nested_term
        
        # Add a noise component to increase difficulty with dynamic scaling
        noise = 0.01 * np.sum(np.random.randn(self.dim) * x * np.cos(10 * x))
        result += noise
        
        # Add a final complex interaction term to increase multimodality
        interaction_term = 0.005 * np.sum(np.sin(100 * x) * np.cos(50 * x))
        result += interaction_term
        
        return result