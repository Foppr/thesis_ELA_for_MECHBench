import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-pi, pi] range for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Sinusoidal component with multiple global minima
        sinusoidal = np.sum(np.sin(4 * scaled_x) * np.cos(3 * scaled_x))
        
        # Quadratic basin component to create wide optima regions
        quadratic = 0.2 * np.sum(x**2)
        
        # Additional harmonic component with higher frequency
        high_freq = 0.07 * np.sum(np.sin(8 * scaled_x) * np.cos(4 * scaled_x))
        
        # Cross-terms to increase interaction between dimensions
        cross_terms = 0.03 * np.sum(x[:-1] * x[1:])
        
        # Add a small noise term to make it non-trivial
        noise = 0.015 * np.sum(np.sin(6 * scaled_x))
        
        # Add a more complex interaction term with mixed frequencies
        complex_interaction = 0.04 * np.sum(np.sin(3 * scaled_x[:-1]) * np.cos(5 * scaled_x[1:]) + np.cos(4 * scaled_x[:-1]) * np.sin(6 * scaled_x[1:]))
        
        # Add a fourth-order polynomial term for increased nonlinearity
        fourth_order = 0.015 * np.sum(x**4)
        
        return sinusoidal + quadratic + high_freq + cross_terms + noise + complex_interaction + fourth_order