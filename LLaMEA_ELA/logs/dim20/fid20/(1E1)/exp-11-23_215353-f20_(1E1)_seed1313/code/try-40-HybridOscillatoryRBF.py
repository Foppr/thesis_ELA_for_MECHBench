import numpy as np

class HybridOscillatoryRBF:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial Basis Function component with multiple centers
        centers = np.linspace(-4.0, 4.0, min(5, self.dim))
        rbf_sum = 0.0
        for i in range(min(5, self.dim)):
            center = centers[i] * np.ones(self.dim)
            rbf_sum += np.exp(-0.5 * np.sum((x - center)**2))
        
        # Sinusoidal oscillation component with varying frequencies
        sin_sum = 0.0
        for i in range(self.dim):
            sin_sum += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i])
        
        # Central attractive force pulling towards origin
        attraction = -0.5 * np.sum(x**2)
        
        # Additional harmonic modulation with exponential decay
        harmonic = np.sum(np.sin(0.5 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Combine components with adaptive weights
        return 0.4 * rbf_sum + 0.3 * sin_sum + 0.2 * attraction + 0.1 * harmonic - 2.0