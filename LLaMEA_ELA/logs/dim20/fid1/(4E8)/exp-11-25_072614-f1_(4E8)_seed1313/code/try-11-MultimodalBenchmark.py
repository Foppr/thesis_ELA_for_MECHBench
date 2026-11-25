import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial multimodal structure with exponential decay
        r = np.sqrt(np.sum(x**2))
        radial_term = np.exp(-r / 2.0) * np.sin(3 * r)
        
        # Multiple global minima in a radial pattern
        minima_penalty = 0.0
        for i in range(1, 6):
            dist_from_min = np.sqrt(np.sum((x - i * np.ones(self.dim))**2))
            minima_penalty += np.exp(-dist_from_min / 0.5) * np.cos(dist_from_min)
        
        # High-dimensional cross-terms
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += x[i] * x[j] * np.sin(0.5 * (x[i] + x[j]))
        
        # Polynomial and sinusoidal components
        poly_term = np.sum(x**6) / 1000.0
        sin_term = np.sum(np.sin(7 * x)) / 10.0
        
        result = radial_term + minima_penalty + cross_term + poly_term + sin_term
        
        return result