import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component with mixed degrees
        poly = np.sum(x**4 + 0.5 * x**3 - 2 * x**2 + x)
        
        # Sinusoidal modulation with varying frequencies
        sin_mod = np.sum(np.sin(1.5 * x) * np.cos(2.5 * x) + np.sin(0.7 * x) * np.cos(1.3 * x))
        
        # Radial basis function component with multiple centers
        rbfs = 0
        centers = np.linspace(-4, 4, min(5, self.dim))
        for i in range(self.dim):
            dist = np.sum((x - centers[i % len(centers)])**2)
            rbfs += np.exp(-0.5 * dist) * np.sin(dist)
        
        # Cross-dimensional interaction term
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, min(i+3, self.dim)):  # Limited interaction
                cross += (x[i] * x[j]) / (1 + abs(x[i] - x[j]))
        
        # Add a global scaling and offset to ensure positive fitness
        return 0.8 * poly + 0.6 * sin_mod + 0.4 * rbfs + 0.3 * cross + 20 * np.sum(np.abs(x)**0.5)