import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-2*pi, 2*pi] range for complex sinusoidal components
        scaled_x = x * 2.0 * np.pi / 5.0
        
        # Multiple nested sinusoidal components with varying frequencies and amplitudes
        sinusoidal = (np.sum(np.sin(5 * scaled_x) * np.cos(4 * scaled_x)) + 
                     0.5 * np.sum(np.sin(9 * scaled_x) * np.cos(7 * scaled_x)) +
                     0.3 * np.sum(np.sin(11 * scaled_x) * np.cos(8 * scaled_x)))
        
        # Quadratic basin component with dimension-dependent scaling
        quadratic = 0.2 * np.sum(x**2)
        
        # Fractal-like cross-terms with non-linear interactions
        cross_terms = 0.1 * np.sum(np.sin(x[:-2] + x[1:-1] + x[2:]) * np.cos(x[:-2] - x[1:-1] + x[2:]))
        
        # Chaotic component with exponential decay and multi-scale structure
        chaotic = 0.05 * np.sum(np.exp(-np.abs(x)) * np.sin(13 * scaled_x))
        
        # Nested harmonic components for increased complexity
        nested_harmonic = 0.03 * np.sum(np.sin(2 * np.sin(3 * scaled_x)) * np.cos(2 * np.cos(4 * scaled_x)))
        
        # Add a small perturbation term to create irregularity
        perturbation = 0.02 * np.sum(np.sin(np.pi * x) * np.cos(np.pi * x))
        
        return sinusoidal + quadratic + cross_terms + chaotic + nested_harmonic + perturbation