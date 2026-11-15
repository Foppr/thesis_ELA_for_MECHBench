import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term
        f1 = np.sum(x_norm**2)
        
        # Multiple sinusoidal modulations with different frequencies
        f2 = np.sum(np.sin(2 * np.pi * x_norm) * np.cos(3 * np.pi * x_norm) * np.exp(-0.5 * np.sum(x_norm**2)))
        
        # Multiple exponential barrier terms with different exponents
        barriers = np.sum(np.exp(-0.2 * np.sum(np.abs(x_norm)**4)) + 0.5 * np.exp(-0.3 * np.sum(np.abs(x_norm)**5)))
        
        # Chaotic component using logistic map-like behavior with multiple iterations
        chaotic = np.sum(np.sin(5 * np.pi * x_norm) * np.cos(7 * np.pi * x_norm) * np.sin(11 * np.pi * x_norm))
        
        # Additional ruggedness term with higher frequency oscillations
        rugged = np.sum(np.sin(10 * np.pi * x_norm) * np.exp(-0.1 * np.sum(x_norm**2)))
        
        # Combine all components with different weights
        return 1.5 * f1 + 3.0 * f2 + 0.8 * barriers + 0.4 * chaotic + 0.6 * rugged