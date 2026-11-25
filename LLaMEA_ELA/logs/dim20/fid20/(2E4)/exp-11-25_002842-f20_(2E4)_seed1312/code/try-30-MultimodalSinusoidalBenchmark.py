import numpy as np

class MultimodalSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-2*pi, 2*pi] range for complex sinusoidal components
        scaled_x = x * 2.0 * np.pi / 5.0
        
        # Enhanced multiple nested sinusoidal components with varying frequencies and amplitudes
        sinusoidal = (np.sum(np.sin(7 * scaled_x) * np.cos(6 * scaled_x)) + 
                     0.6 * np.sum(np.sin(13 * scaled_x) * np.cos(11 * scaled_x)) +
                     0.4 * np.sum(np.sin(17 * scaled_x) * np.cos(14 * scaled_x)))
        
        # Quadratic basin component with dimension-dependent scaling
        quadratic = 0.25 * np.sum(x**2)
        
        # Enhanced fractal-like cross-terms with non-linear interactions and increased complexity
        cross_terms = 0.15 * np.sum(np.sin(x[:-2] + x[1:-1] + x[2:]) * np.cos(x[:-2] - x[1:-1] + x[2:]))
        
        # Chaotic component with exponential decay and multi-scale structure
        chaotic = 0.08 * np.sum(np.exp(-np.abs(x)) * np.sin(17 * scaled_x))
        
        # Enhanced nested harmonic components for increased complexity
        nested_harmonic = 0.05 * np.sum(np.sin(3 * np.sin(4 * scaled_x)) * np.cos(3 * np.cos(5 * scaled_x)))
        
        # Enhanced perturbation term to create irregularity and increase difficulty
        perturbation = 0.03 * np.sum(np.sin(np.pi * x) * np.cos(np.pi * x) * np.sin(2 * x))
        
        # Additional cross-dimensional interaction terms for increased complexity
        interaction_terms = 0.02 * np.sum(np.sin(x[:-1] * x[1:]) * np.cos(x[:-1] + x[1:]))
        
        # Introduce a small mutation: slightly modify the chaotic component's frequency and amplitude
        mutated_chaotic = 0.09 * np.sum(np.exp(-np.abs(x)) * np.sin(19 * scaled_x))
        
        return sinusoidal + quadratic + cross_terms + mutated_chaotic + nested_harmonic + perturbation + interaction_terms