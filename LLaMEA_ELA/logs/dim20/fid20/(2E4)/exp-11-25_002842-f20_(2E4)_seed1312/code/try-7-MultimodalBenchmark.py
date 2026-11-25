import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms (global minimum at origin)
        quadratic = np.sum(x_norm**2)
        
        # Enhanced sinusoidal terms with higher frequency and amplitude modulation
        sinusoidal = np.sum((np.sin(7 * np.pi * x_norm) ** 2) * (1 + 0.5 * np.abs(x_norm)))
        
        # Additional radial quadratic term to create a more complex basin
        radial_quadratic = 0.3 * (np.sum(x_norm**2))**2
        
        # Penalty term for large values with different exponent
        penalty = 0.2 * np.sum(np.abs(x_norm)**4)
        
        return quadratic + sinusoidal + radial_quadratic + penalty