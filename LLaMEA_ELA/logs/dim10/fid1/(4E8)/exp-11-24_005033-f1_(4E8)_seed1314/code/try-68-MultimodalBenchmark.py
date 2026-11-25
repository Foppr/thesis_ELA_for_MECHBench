import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Spiral-like structure with nested harmonics
        spiral_term = 0.0
        for i in range(self.dim):
            xi = x[i]
            spiral_term += (xi**2 + 1e-8) * np.sin(14 * np.pi * xi) * np.cos(5 * np.pi * xi)
        
        # Dynamic conditioning based on dimension
        condition_term = 0.0
        for i in range(self.dim):
            condition_term += (i + 1) * x[i]**4
        
        # Adaptive noise component
        noise_term = 0.0
        for i in range(self.dim):
            noise_term += np.sin(23 * x[i]) * np.cos(19 * x[i]) * (1.0 / (1.0 + np.exp(-x[i]**2)))
        
        # Cross-dimensional coupling with spiral interaction
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.cos(0.8 * (x[i]**2 + x[j]**2)) * \
                              np.exp(-0.12 * (x[i]**2 + x[j]**2))
        
        # Combined result
        result = spiral_term + condition_term + noise_term + 0.5 * cross_term
        
        # Add global minimum at origin with penalty for distance from origin
        result += 0.18 * np.sum(x**6) + 0.09 * np.sum(np.abs(x)**3)
        
        return result