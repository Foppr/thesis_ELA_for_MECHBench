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
            oscillation += np.sin(2.0 * np.pi * x[i]) * np.cos(3.0 * np.pi * x[i])
            
        # Polynomial repulsion terms to create irregular local minima
        repulsion = 0.0
        for i in range(self.dim):
            repulsion += 0.5 * (x[i] ** 4) - 2.0 * (x[i] ** 2) + 1.0
            
        # Chaotic component using a logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10.0 * x[i]) * np.cos(7.0 * x[i])
            
        # Combine all components with different weights
        return 0.3 * oscillation + 0.4 * repulsion + 0.3 * chaotic