import numpy as np

class ChaoticBasinBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = np.zeros(dim)
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension mismatch")
        
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Radial basin component with chaotic modulation
        radius = np.linalg.norm(x_norm)
        basin_term = radius**2 * (1 + 0.5 * np.sin(10 * radius))
        
        # Sinusoidal oscillations in multiple directions
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(3 * x_norm[i]) * np.cos(2 * x_norm[(i + 1) % self.dim])
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(5 * x_norm[i] * (1 - x_norm[i]**2))
        
        return basin_term + 0.3 * oscillation + 0.1 * chaotic