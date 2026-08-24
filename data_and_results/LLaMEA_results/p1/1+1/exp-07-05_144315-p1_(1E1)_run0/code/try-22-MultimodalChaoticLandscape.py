import numpy as np

class MultimodalChaoticLandscape:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basis function component with multiple centers
        rbf = 0.0
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        for i in range(len(centers)):
            if i < self.dim:
                rbf += np.exp(-0.5 * (x[i] - centers[i%len(centers)])**2 / (0.5**2))
        
        # Sinusoidal oscillations with varying frequencies and amplitudes
        sin_osc = 0.0
        for i in range(self.dim):
            sin_osc += np.sin(2 * np.pi * x[i]) * np.cos(3 * np.pi * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Cross-term interactions creating complex landscape
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1 + np.abs(x[i] - x[j]))
        
        # Polynomial terms for additional curvature
        poly_term = 0.05 * np.sum(x**4) + 0.1 * np.sum(x**6)
        
        # Chaotic modulation with exponential decay
        chaotic_mod = 0.0
        for i in range(self.dim):
            chaotic_mod += np.sin(x[i]) * np.cos(2 * x[i]) * np.exp(-0.05 * x[i]**2)
        
        # Global scaling based on distance from origin
        dist_from_origin = np.sqrt(np.sum(x**2))
        scaling = 1.0 + 0.2 * np.sin(0.5 * dist_from_origin)
        
        return rbf + 0.5 * sin_osc + 0.3 * cross_term + poly_term + 0.4 * chaotic_mod + scaling