import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic logistic map component with varying r parameters
        logistic_terms = 0.0
        for i in range(self.dim):
            r = 3.9 + 0.1 * np.sin(i * 0.7)
            xi = 0.5 + 0.1 * np.cos(i * 0.3)
            logistic_terms += r * xi * (1 - xi)
        
        # Spherical harmonics with varying degrees and orders
        sph_harmonics = 0.0
        for i in range(self.dim):
            degree = int(2 + i % 3)
            order = int(i % (degree + 1))
            sph_harmonics += np.sin(degree * np.arctan2(x[i], x[(i+1)%self.dim])) * np.cos(order * np.arctan2(x[i], x[(i+1)%self.dim]))
        
        # Adaptive noise injection with dynamic amplitude scaling
        noise_amp = 0.5 * (1 + np.sin(np.sum(x**2) * 0.1))
        noise_terms = noise_amp * np.sum(np.random.normal(0, 0.1, self.dim)**2)
        
        # Mixed integer-nonlinear interactions with piecewise functions
        mixed_terms = 0.0
        for i in range(self.dim):
            if x[i] > 0:
                mixed_terms += (x[i]**3) * np.sin(x[i])
            else:
                mixed_terms += (x[i]**2) * np.cos(x[i])
        
        # Cross-dimensional polynomial interactions with irrational coefficients
        poly_cross = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            poly_cross += np.sin(np.pi * np.sqrt(x[i]**2 + x[j]**2)) * (x[i]**np.e + x[j]**np.pi)
        
        # Combined function value
        return logistic_terms + sph_harmonics + noise_terms + mixed_terms + poly_cross