import numpy as np

class MultimodalCrossInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        global_min = 0.0
        
        # Sinusoidal terms creating multiple local minima
        sin_terms = 0.0
        for i in range(self.dim):
            sin_terms += np.sin(2.0 * x[i]) * np.cos(1.5 * x[i])
        
        # Polynomial penalty terms to increase complexity
        poly_terms = 0.0
        for i in range(self.dim):
            poly_terms += 0.1 * x[i]**4 + 0.05 * x[i]**3
        
        # Cross-dimensional interaction terms
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.2 * np.sin(0.5 * x[i]) * np.cos(0.3 * x[j]) * (x[i] + x[j])**2
        
        # Distance-based penalty to encourage convergence
        distance_penalty = 0.01 * np.sum(x**2)
        
        return sin_terms + poly_terms + cross_terms + distance_penalty