import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Quadratic base with sinusoidal modulation
        quadratic_base = np.sum(x_norm**2 * (1 + 0.2 * np.sin(10 * x_norm)))
        
        # Radial component with multiple frequency harmonics
        r = np.sqrt(np.sum(x_norm**2))
        radial_term = -np.exp(-r**2) + 0.5 * np.sin(15 * r) + 0.3 * np.cos(20 * r) + 0.1 * np.sin(25 * r)
        
        # Cross-dimensional coupling with polynomial interaction
        coupling = 0.0
        for i in range(self.dim):
            j = (i + 1) % self.dim
            coupling += x_norm[i] * x_norm[j] * np.sin(7 * (x_norm[i] + x_norm[j]))
        coupling = coupling / self.dim
        
        # Multi-scale oscillatory component with exponential decay
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(12 * x_norm[i]) * np.cos(9 * x_norm[i]) * np.exp(-0.1 * np.abs(x_norm[i]))
        
        # Chaotic perturbation with high frequency and nonlinearity
        chaotic = 0.05 * np.sum(np.sin(30 * x_norm) * np.cos(25 * x_norm) * (1 + 0.1 * x_norm**4))
        
        # Final combined function
        return quadratic_base + radial_term + coupling + oscillation + chaotic