import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with higher-order interactions
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Modified sinusoidal oscillations with varied frequencies and amplitudes
        sinusoidal = 2.0 * np.sum(np.sin(8.0 * x)) + 1.5 * np.sum(np.sin(3.0 * x)**2) + 0.8 * np.sum(np.cos(4.0 * x))
        
        # Complex cross-term interactions with non-linear coupling
        cross_terms = 0.2 * np.sum(x[:-1] * x[1:]**2) + 0.1 * np.sum(x[:-2] * x[2:]**3) + 0.05 * np.sum((x[:-1] + x[1:])**4)
        
        # Additional challenge through interaction between all dimensions
        interaction = 0.02 * np.sum(np.outer(x, x).flatten()**2)
        
        return polynomial + sinusoidal + cross_terms + interaction