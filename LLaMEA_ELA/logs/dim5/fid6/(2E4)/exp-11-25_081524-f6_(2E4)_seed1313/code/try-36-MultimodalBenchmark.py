import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic oscillations with varying amplitudes and frequencies
        periodic = np.sum(np.sin(3 * np.pi * x) * np.cos(2 * np.pi * x)) + \
                   0.7 * np.sum(np.sin(5 * np.pi * x) * np.cos(4 * np.pi * x))
        
        # Saddle point structure with quadratic and quartic terms
        saddle = np.sum(x**2 - 0.15 * x**4)
        
        # Adaptive conditioning based on dimensionality
        adaptive = np.sum((x**2 + 0.02 * x**6) * (1 + 0.15 * self.dim * np.sin(x)))
        
        # Cross-dimensional interaction terms with exponential decay
        cross_terms = 0.4 * np.sum(np.exp(-0.15 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Asymmetric valley structure with varying steepness
        valley = np.sum((x - np.sin(0.6 * x))**2) + 0.3 * np.sum(np.abs(x[:-2] - 2*x[1:-1] + x[2:])**2)
        
        return periodic + saddle + adaptive + cross_terms + valley