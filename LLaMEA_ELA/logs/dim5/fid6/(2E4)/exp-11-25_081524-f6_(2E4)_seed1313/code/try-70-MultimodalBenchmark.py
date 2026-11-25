import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term with logarithmic conditioning
        quadratic = np.sum(x**2) * (1.0 + 0.1 * np.log(self.dim + 1))
        
        # Saddle-point inducing term with hyperbolic tangent
        saddle = np.sum(np.tanh(x)**2 - 0.5 * x**2)
        
        # Multi-scale sinusoidal modulations with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        sin_modulation = np.sum(np.sin(freqs * x) * np.cos(freqs * x * 0.5))
        
        # Logarithmic barrier to prevent boundary escape
        barrier = np.sum(1.0 / (1.0 + np.exp(-x)) * (5.0 - np.abs(x)))
        
        # Chaotic interaction using a simple iterative map
        chaotic_interaction = 0.0
        for i in range(self.dim):
            if i < self.dim - 1:
                chaotic_interaction += np.sin(x[i] * x[i+1]) * np.exp(-0.1 * (x[i]**2 + x[i+1]**2))
        
        # Adaptive ridge structure with exponential decay
        ridge = 0.05 * np.sum(np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Fractional polynomial interaction
        poly_frac = 0.01 * np.sum(x**(1.5) + 0.3 * x**(2.5))
        
        return quadratic + saddle + sin_modulation + barrier + chaotic_interaction + ridge + poly_frac