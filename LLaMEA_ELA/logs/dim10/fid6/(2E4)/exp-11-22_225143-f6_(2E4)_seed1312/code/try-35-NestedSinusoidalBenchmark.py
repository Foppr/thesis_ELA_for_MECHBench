import numpy as np

class NestedSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Base quadratic term with conditioning
        f_val = 0.2 * np.sum(x_norm**2)
        
        # Nested parabolic wells with varying depths and positions
        for i in range(self.dim):
            # Create nested wells with different scales and positions
            well_depth = 0.6 * (1 + np.sin(i * np.pi / 5))
            well_scale = 1.2 + 0.3 * np.cos(i * np.pi / 4)
            center = np.sin(i * np.pi / self.dim) * 0.8
            f_val += well_depth * np.exp(-well_scale * np.sum((x_norm - center)**2))
        
        # Sinusoidal modulations with varying frequencies and amplitudes
        for i in range(self.dim):
            f_val += 0.35 * np.sin(4 * np.pi * x_norm[i]) * np.cos(3 * np.pi * x_norm[i])
            f_val += 0.25 * np.sin(6 * np.pi * x_norm[i]**2) * np.cos(5 * np.pi * x_norm[i])
        
        # Cross-dimensional interaction terms with more complex coupling
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Reduced cross-dimensionality
                f_val += 0.2 * np.sin(3 * np.pi * (x_norm[i] + x_norm[j])) * np.cos(4 * np.pi * (x_norm[i] - x_norm[j]))
                f_val += 0.15 * np.cos(5 * np.pi * (x_norm[i]**2 + x_norm[j]**2)) * np.sin(2 * np.pi * (x_norm[i]*x_norm[j]))
        
        # Higher-order polynomial interactions with more varied exponents
        for i in range(self.dim):
            f_val += 0.08 * (x_norm[i]**3 + x_norm[i]**5) * np.sin(7 * np.pi * x_norm[i])
        
        # Multi-scale periodic components with different frequencies and phases
        f_val += 0.25 * np.sum(np.sin(9 * np.pi * x_norm) * np.cos(8 * np.pi * x_norm))
        f_val += 0.2 * np.sum(np.sin(7 * np.pi * x_norm**2) * np.cos(6 * np.pi * x_norm**2))
        
        # Chaotic cross-dimensional coupling with exponential decay
        f_val += 0.15 * np.sum(np.sin(4 * np.pi * x_norm) * np.cos(5 * np.pi * x_norm) * np.exp(-0.5 * x_norm**2))
        
        return f_val