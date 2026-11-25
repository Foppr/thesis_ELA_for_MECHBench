import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component
        base = np.sum(x**2)
        
        # Fractal sine modulation with recursive structure
        fractal = 0.0
        for i in range(self.dim):
            mod = 1.0
            for depth in range(3):  # Recursive modulation
                mod *= np.sin(2**(depth+1) * np.pi * x[i] / (2**depth + 1))
            fractal += mod * np.exp(-0.1 * x[i]**2)
        
        # Adaptive curvature based on dimensionality and position
        adaptive_curvature = 0.0
        for i in range(self.dim):
            # Dynamic scaling factor per dimension
            scale = 1.0 + 0.5 * np.sin(0.3 * i + np.sum(x))
            adaptive_curvature += scale * (x[i]**6) * np.cos(0.2 * x[i])
        
        # Self-similar cross-dimensional interactions
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                # Distance-based coupling with fractal scaling
                dist = np.abs(x[i] - x[j])
                coupling = np.sin(np.pi * dist) * np.exp(-dist**2 / 10.0)
                cross_terms += coupling * (x[i]**3 + x[j]**3)
        
        # Dynamic dimension coupling with periodic modulation
        coupling_factor = 0.0
        for i in range(self.dim):
            coupling_factor += np.sin(0.5 * np.pi * (i + 1) / self.dim) * x[i]
        
        # Combined function with fractal characteristics
        return base + 0.3 * fractal + 0.2 * adaptive_curvature + 0.1 * cross_terms + 0.05 * coupling_factor**2