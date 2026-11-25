import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced polynomial terms with exponential scaling
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(np.exp(0.5 * np.abs(x)) - 1)
        
        # Highly oscillatory sinusoidal components with varying frequencies and amplitudes
        sinusoidal = np.sum(np.sin(10.0 * x)) + 0.7 * np.sum(np.sin(5.0 * x)**2) + 0.3 * np.sum(np.sin(2.0 * x)**3)
        
        # Complex cross-terms with exponential coupling and higher-order interactions
        cross_terms = 0.2 * np.sum(x[:-2] * np.exp(-0.1 * x[2:])) + 0.1 * np.sum((x[:-1] + x[1:])**4) + 0.05 * np.sum(x**6)
        
        # Novel asymmetric interaction term with exponential weighting
        asymmetric_cross = 0.1 * np.sum(np.exp(0.2 * x[:-1]) * x[1:]**2) + 0.08 * np.sum(x[:-2] * np.sin(3.0 * x[2:]))
        
        # Additional challenge through a combination of polynomial and exponential interactions
        mixed_interaction = 0.03 * np.sum(np.exp(0.1 * x**2) * x**3)
        
        return polynomial + sinusoidal + cross_terms + asymmetric_cross + mixed_interaction