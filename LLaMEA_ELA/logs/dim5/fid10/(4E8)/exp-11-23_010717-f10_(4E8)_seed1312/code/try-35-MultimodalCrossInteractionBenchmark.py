import numpy as np

class MultimodalCrossInteractionBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        global_min = 0.0
        
        # Sinusoidal terms creating multiple local minima with higher frequency
        sin_terms = 0.0
        for i in range(self.dim):
            sin_terms += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Polynomial penalty terms with increased complexity
        poly_terms = 0.0
        for i in range(self.dim):
            poly_terms += 0.15 * x[i]**4 + 0.1 * x[i]**3 + 0.05 * x[i]**2
        
        # Cross-dimensional interaction terms with different coupling strengths
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_terms += 0.3 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[j]) * (x[i]**2 + x[j]**2)
        
        # Distance-based penalty to encourage convergence
        distance_penalty = 0.015 * np.sum(x**2)
        
        return sin_terms + poly_terms + cross_terms + distance_penalty