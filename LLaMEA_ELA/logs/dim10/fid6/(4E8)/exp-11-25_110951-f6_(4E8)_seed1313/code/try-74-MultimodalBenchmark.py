import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Nested sinusoidal oscillations with varying frequencies and amplitudes
        nested_sin = np.sum(np.sin(2 * np.pi * (x_normalized + 0.1)) * 
                           np.sin(4 * np.pi * (x_normalized + 0.1)) * 
                           np.sin(8 * np.pi * (x_normalized + 0.1)))
        
        # Adaptive conditioning factor that increases with dimensionality
        condition_factor = 1.0 + 0.3 * (self.dim - 1)
        
        # Fractal-like basin term with nested exponential decay and shifted center
        r = np.sqrt(np.sum(x_normalized**2))
        basin_term = 0.5 * np.exp(-r**2) * np.prod(np.cos(3 * np.pi * x_normalized)) + \
                     0.2 * np.exp(-0.5 * r**2) * np.sum(np.sin(6 * np.pi * (x_normalized + 0.2)))
        
        # Multi-scale interaction terms with chaotic modulation
        interaction_term = 0.3 * np.sum((x_normalized**4) * 
                                       np.cos(3 * np.pi * x_normalized) * 
                                       np.sin(5 * np.pi * x_normalized))
        
        # Cross-dimensional coupling with varying strength based on position
        cross_coupling = 0.25 * np.sum(np.sin(2 * np.pi * x_normalized[:-1]) * 
                                     np.cos(2 * np.pi * x_normalized[1:]) * 
                                     (1 + 0.2 * np.sin(4 * np.pi * x_normalized[:-1])))
        
        # Chaotic perturbation with fractal-like structure and modified frequency
        chaos_perturbation = 0.1 * np.sum(np.sin(7 * x_normalized) * 
                                         np.cos(7 * x_normalized) * 
                                         np.exp(-0.3 * (x_normalized**2)))
        
        # Combined fitness function with adaptive scaling
        return condition_factor * (nested_sin + basin_term + interaction_term + 
                                 cross_coupling + chaos_perturbation)