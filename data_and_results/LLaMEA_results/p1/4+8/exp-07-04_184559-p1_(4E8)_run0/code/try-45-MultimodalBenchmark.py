import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Product of sinusoidal terms with higher frequency and additional modulation
        sinusoidal = np.prod(np.sin(7 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm))
        
        # Add a penalty term for large values with modified exponent
        penalty = 0.15 * np.sum(x_norm**6)
        
        # Add radial bias term to increase conditioning difficulty
        radial_bias = 0.05 * np.sum(x_norm**4)
        
        # Combine terms to create a challenging landscape
        return quadratic + 15 * sinusoidal + penalty + radial_bias