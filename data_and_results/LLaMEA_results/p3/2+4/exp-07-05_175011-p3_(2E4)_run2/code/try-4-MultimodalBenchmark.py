import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_norm**2)
        
        # Sum of sinusoidal terms with higher frequency and amplitude to create more local minima
        sinusoidal = np.sum(np.sin(7 * np.pi * x_norm)**3)
        
        # Additional penalty term to encourage convergence to origin with modified exponent
        penalty = 0.15 * np.sum(x_norm**4)
        
        # Add a small shift to the global minimum to increase difficulty
        shift = 0.05 * np.sum((x_norm - 0.2)**2)
        
        return quadratic + sinusoidal + penalty + shift