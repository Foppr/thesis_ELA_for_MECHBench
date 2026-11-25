import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic tent map component with parameter modulation
        tent_component = 0
        a = 1.7  # chaotic parameter
        for i in range(self.dim):
            if x[i] < 0.5:
                tent_val = a * x[i]
            else:
                tent_val = a * (1 - x[i])
            tent_component += tent_val**2
        
        # Spherical harmonic interaction terms
        sph_harm = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 1e-8)
                sph_harm += np.sin(2 * np.pi * dist) * np.cos(3 * np.pi * dist)
        
        # Adaptive polynomial penalty with dimension-dependent weights
        poly_penalty = 0
        for i in range(self.dim):
            weight = 1.0 + 0.5 * np.sin(0.3 * i)
            term = weight * (x[i]**4 - 6 * x[i]**2 + 8)
            poly_penalty += term
        
        # Cross-dimensional coupling with dynamic interaction strengths
        coupling = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                coupling += (x[i] * x[j]) / (1 + 0.2 * np.abs(x[i] - x[j])**1.5)
        
        # Gaussian mixture with varying variances and centers
        gaussian_mixture = 0
        centers = np.linspace(-4, 4, 5)
        for center in centers:
            gaussian_mixture += np.exp(-0.5 * ((x - center) / (1.5 + 0.2 * np.sin(0.5 * center)))**2)
        
        # Combine all components with optimized weights
        return 0.8 * tent_component + 1.5 * sph_harm + 1.0 * poly_penalty + 0.6 * coupling + 0.9 * gaussian_mixture + 2.5 * self.dim