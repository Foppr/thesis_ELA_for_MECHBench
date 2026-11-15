import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        quadratic = np.sum(x_norm**2)
        
        # Product of sinusoidal terms with varying frequencies to create multiple local minima
        sinusoidal = np.prod(np.sin(3 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm))
        
        # Add a penalty term for large values to encourage convergence to origin
        penalty = 0.1 * np.sum(x_norm**4)
        
        # Add radial bias term to increase conditioning difficulty
        radial_bias = 0.5 * np.sum(x_norm**6)
        
        # Add a second sinusoidal modulation with different phase to increase complexity
        phase_mod = np.sin(2 * np.pi * np.sum(x_norm**2))
        
        # Combine all terms to create a challenging landscape
        return quadratic + 15 * sinusoidal + penalty + radial_bias + 2 * phase_mod