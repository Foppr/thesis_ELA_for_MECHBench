import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial terms with higher order components
        polynomial = np.sum(x**2) + 0.1 * np.sum(x**4) + 0.01 * np.sum(x**6)
        
        # Sinusoidal oscillations with varying frequencies
        sinusoidal = np.sum(np.sin(3.0 * x) * np.cos(7.0 * x)) * np.exp(-0.05 * np.sum(x**2))
        
        # Radial basis function components for complex landscape
        rbf = np.sum(np.exp(-0.5 * (x**2 + 1.0))) * 0.5
        
        # Cross-term interactions with non-linear coupling
        cross_terms = np.sum(np.sin(x[:-1] + x[1:])) * 0.3
        
        # Additional harmonic modulation
        harmonic_mod = np.sum(np.sin(2.0 * x) * np.cos(4.0 * x)) * 0.2
        
        return polynomial + sinusoidal + cross_terms + rbf + harmonic_mod