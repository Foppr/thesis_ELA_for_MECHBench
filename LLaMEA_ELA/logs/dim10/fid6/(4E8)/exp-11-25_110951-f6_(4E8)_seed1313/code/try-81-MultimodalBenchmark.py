import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_normalized = x / 5.0
        
        # Enhanced nested sinusoidal oscillations with fractal-like frequency modulation
        freq_modulation = np.prod(1 + 0.2 * np.sin(5 * np.pi * x_normalized))
        nested_sin = np.sum(np.sin(freq_modulation * 2 * np.pi * (x_normalized + 0.1)) * 
                           np.sin(freq_modulation * 4 * np.pi * (x_normalized + 0.1)) * 
                           np.sin(freq_modulation * 8 * np.pi * (x_normalized + 0.1)))
        
        # Adaptive conditioning factor that increases with dimensionality
        condition_factor = 1.0 + 0.5 * (self.dim - 1)
        
        # Fractal-like basin term with multi-scale exponential decay and shifted center
        r = np.sqrt(np.sum(x_normalized**2))
        basin_term = 0.6 * np.exp(-r**2) * np.prod(np.cos(3 * np.pi * x_normalized)) + \
                     0.3 * np.exp(-0.3 * r**2) * np.sum(np.sin(7 * np.pi * (x_normalized + 0.2)))
        
        # Multi-scale interaction terms with chaotic modulation and variable coupling strength
        interaction_term = 0.4 * np.sum((x_normalized**3) * 
                                       np.cos(4 * np.pi * x_normalized) * 
                                       np.sin(6 * np.pi * x_normalized))
        
        # Cross-dimensional coupling with dynamic strength based on position and dimension
        cross_coupling = 0.3 * np.sum(np.sin(3 * np.pi * x_normalized[:-1]) * 
                                     np.cos(3 * np.pi * x_normalized[1:]) * 
                                     (1 + 0.3 * np.sin(5 * np.pi * x_normalized[:-1])) * 
                                     (1 + 0.1 * self.dim))
        
        # Chaotic perturbation with enhanced fractal structure and frequency modulation
        chaos_perturbation = 0.15 * np.sum(np.sin(8 * x_normalized) * 
                                          np.cos(8 * x_normalized) * 
                                          np.exp(-0.4 * (x_normalized**2)) * 
                                          np.sin(3 * np.pi * x_normalized))
        
        # Combined fitness function with enhanced scaling and modified balance
        return condition_factor * (nested_sin + basin_term + interaction_term + 
                                 cross_coupling + chaos_perturbation)