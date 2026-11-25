import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Enhanced periodic oscillations with higher frequencies and modified amplitudes
        periodic = 1.5 * np.sum(np.sin(3 * np.pi * x) * np.cos(4 * np.pi * x)) + \
                   0.8 * np.sum(np.sin(5 * np.pi * x) * np.cos(6 * np.pi * x))
        
        # Saddle point structure with cubic and quintic terms for increased complexity
        saddle = np.sum(x**2 - 0.15 * x**3 + 0.02 * x**5)
        
        # Adaptive conditioning with exponential scaling based on dimensionality
        adaptive = np.sum((x**2 + 0.02 * x**6) * (1 + 0.15 * self.dim * np.sin(0.5 * x)))
        
        # Enhanced cross-dimensional interaction terms with stronger decay
        cross_terms = 0.5 * np.sum(np.exp(-0.15 * np.abs(x[:-1] - x[1:])) * (x[:-1]**2 + x[1:]**2))
        
        # Asymmetric valley structure with increased steepness and higher-order differences
        valley = np.sum((x - np.sin(0.7 * x))**2) + 0.3 * np.sum(np.abs(x[:-2] - 2*x[1:-1] + x[2:])**2)
        
        return periodic + saddle + adaptive + cross_terms + valley