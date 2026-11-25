import numpy as np

class MultimodalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Central quadratic basin term
        basin = 0.1 * np.sum(x**2)
        
        # Sinusoidal oscillations in each dimension
        oscillation = np.sum(np.sin(2 * np.pi * x) ** 2)
        
        # Cross-dimensional interaction terms
        cross_interaction = 0.5 * np.sum((x[:-1] - x[1:]) ** 2)
        
        # Boundary repulsion effect
        boundary_penalty = np.sum(np.maximum(0, 5.0 - np.abs(x)) ** 3)
        
        # Additional high-frequency oscillation
        high_freq = 0.3 * np.sum(np.sin(10 * np.pi * x) ** 2)
        
        return basin + oscillation + cross_interaction + boundary_penalty + high_freq