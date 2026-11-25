import numpy as np

class MultimodalOscillatoryBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        x = np.array(x)
        
        # Central quadratic basin term
        basin = 0.1 * np.sum(x**2)
        
        # Sinusoidal oscillations in each dimension with modified frequency
        oscillation = np.sum(np.sin(3 * np.pi * x) ** 2)
        
        # Enhanced cross-dimensional interaction terms
        cross_interaction = 0.7 * np.sum((x[:-1] - x[1:]) ** 2)
        
        # Strengthened boundary repulsion effect
        boundary_penalty = np.sum(np.maximum(0, 5.0 - np.abs(x)) ** 4)
        
        # Additional high-frequency oscillation with modified coefficient
        high_freq = 0.4 * np.sum(np.sin(15 * np.pi * x) ** 2)
        
        # Cross-dimensional quadratic coupling term
        coupling = 0.2 * np.sum(x[:-1] * x[1:])
        
        return basin + oscillation + cross_interaction + boundary_penalty + high_freq + coupling