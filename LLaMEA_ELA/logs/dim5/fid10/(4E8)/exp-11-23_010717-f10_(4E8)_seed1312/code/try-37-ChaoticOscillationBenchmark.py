import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] if not already
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation component with varying frequencies
        oscillation = 0.0
        for i in range(self.dim):
            oscillation += np.sin(2.5 * np.pi * x[i]) * np.cos(3.5 * np.pi * x[i])
            
        # Polynomial repulsion terms to create irregular local minima
        repulsion = 0.0
        for i in range(self.dim):
            repulsion += 0.6 * (x[i] ** 4) - 2.5 * (x[i] ** 2) + 1.2
            
        # Chaotic component using a logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(9.0 * x[i]) * np.cos(6.0 * x[i])
            
        # Cross-dimensional interaction terms
        cross_interaction = 0.0
        for i in range(self.dim - 1):
            cross_interaction += 0.1 * x[i] * x[i+1] * np.sin(np.pi * (x[i] + x[i+1]))
            
        # Combine all components with different weights
        return 0.35 * oscillation + 0.35 * repulsion + 0.25 * chaotic + 0.05 * cross_interaction