import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Sinusoidal component with multiple global minima
        sinusoidal = np.sum(np.sin(3 * scaled_x) * np.cos(2 * scaled_x))
        
        # Quadratic basin component to create wide optima regions
        quadratic = 0.15 * np.sum(x**2)
        
        # Additional harmonic component to increase complexity
        harmonic = 0.05 * np.sum(np.sin(4 * scaled_x) * np.cos(3 * scaled_x))
        
        # Cross-terms to introduce interactions between dimensions
        cross_terms = 0.02 * np.sum(x[:-1] * x[1:])
        
        # Add a small noise term to make it non-trivial
        noise = 0.01 * np.sum(np.sin(7 * scaled_x))
        
        return sinusoidal + quadratic + harmonic + cross_terms + noise