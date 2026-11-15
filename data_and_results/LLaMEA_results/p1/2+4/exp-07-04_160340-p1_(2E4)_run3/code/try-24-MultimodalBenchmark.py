import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_global = np.zeros(dim)
    
    def f(self, x):
        # Normalize input to [-5, 5] domain
        x = np.array(x)
        
        # Apply chaotic perturbation to create complex landscape
        chaotic_factor = 0.1 * np.sin(10.0 * x) * np.cos(5.0 * x)
        
        # Shift variables to center the function
        shifted_x = x - 1.0
        
        # Calculate multiple sinusoidal components with varying frequencies
        term1 = np.sum(shifted_x**2)
        term2 = np.sum(np.sin(np.sqrt(np.abs(shifted_x) + 1e-8))**2)
        term3 = 0.1 * np.sum(shifted_x**4)
        
        # Add chaotic sinusoidal perturbations
        perturbation = np.sum(chaotic_factor**2)
        
        # Add multiple nested global minima at different locations
        minima_locations = [
            np.array([1.0] * self.dim),
            np.array([-1.0] * self.dim),
            np.array([0.5] * self.dim),
            np.array([-0.5] * self.dim),
            np.array([2.0] * self.dim),
            np.array([-2.0] * self.dim)
        ]
        
        # Calculate distance to each minimum and add penalty
        penalty = 0
        for i, loc in enumerate(minima_locations):
            # Varying penalty strength for different minima
            strength = 0.5 + 0.2 * np.sin(i)
            penalty += strength * np.exp(-np.sum((shifted_x - loc)**2) / 5.0)
        
        # Combine all terms with additional complexity
        result = term1 + term2 + term3 + perturbation - penalty
        
        # Add a small noise term to make the landscape even more challenging
        noise = 0.01 * np.random.random()
        
        return result + noise