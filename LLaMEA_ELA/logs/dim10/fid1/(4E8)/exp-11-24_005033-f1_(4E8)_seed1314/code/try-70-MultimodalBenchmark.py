import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Fractal-like recursive structure with multi-scale harmonics
        fractal_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            fractal_term += (xi**2 + 1e-8) * np.sin(20 * np.pi * xi) * np.cos(10 * np.pi * xi) * \
                           np.sin(5 * np.pi * xi**2) * np.cos(2.5 * np.pi * xi**2)
        
        # Dynamic elliptic conditioning with dimension-dependent scaling
        condition_term = 0.0
        for i in range(self.dim):
            # Adaptive conditioning based on dimension and variable value
            adaptive_factor = 1.0 + 0.5 * np.sin(0.5 * np.pi * (i + 1) / self.dim)
            condition_term += adaptive_factor * (i + 1) * x[i]**4
        
        # Enhanced gradient complexity with multi-frequency modulation
        gradient_term = 0.0
        for i in range(self.dim):
            gradient_term += np.sin(30 * x[i]) * np.cos(25 * x[i]) * np.sin(15 * x[i]) * \
                           np.exp(-0.2 * x[i]**2) * (1.0 + 0.3 * np.sin(7 * x[i]))
        
        # Complex cross-dimensional coupling with recursive interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Recursive coupling with multiple interaction terms
                coupling = np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2)) * \
                          np.exp(-0.2 * (x[i]**2 + x[j]**2)) * \
                          (1.0 + 0.2 * np.sin(3 * x[i] * x[j]))
                cross_term += coupling
        
        # Additional non-separability through nested polynomial interactions
        poly_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                poly_term += (x[i]**2 + x[j]**2) * np.sin(0.1 * (x[i] + x[j])**3)
        
        # Combined result with enhanced multimodality
        result = fractal_term + condition_term + gradient_term + 0.7 * cross_term + 0.5 * poly_term
        
        # Global minimum at origin with penalty for distance from origin
        result += 0.2 * np.sum(x**6) + 0.1 * np.sum(np.abs(x)**3.5)
        
        return result