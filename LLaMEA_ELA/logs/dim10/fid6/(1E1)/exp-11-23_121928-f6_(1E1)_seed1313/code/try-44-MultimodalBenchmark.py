import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Radial component with multiple peaks
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = np.sin(10 * np.pi * r) * np.exp(-r**2 / 2.0)
        
        # Angular components creating directional complexity
        angles = np.arctan2(x_norm[1], x_norm[0]) if self.dim > 1 else 0.0
        angular_term = np.cos(5 * angles) + 0.5 * np.sin(3 * angles)
        
        # Multi-scale periodicity with varying frequencies
        periodic_terms = []
        for i in range(self.dim):
            freq = 2**(i % 3 + 1)
            periodic_terms.append(np.sin(freq * np.pi * x_norm[i]) * np.cos(freq * np.pi * x_norm[i]))
        
        # Adaptive conditioning based on dimensionality
        condition_factor = 1.0 + 0.1 * np.log(self.dim + 1)
        
        # Interaction terms between dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_norm[i]**2 + x_norm[j]**2) * np.sin(np.pi * (x_norm[i] - x_norm[j])**2)
        
        # Combined function with competing forces
        return condition_factor * (0.5 * radial_term + 0.3 * angular_term + 
                                  0.1 * np.sum(periodic_terms) + 0.05 * interaction) + 0.01 * r**4