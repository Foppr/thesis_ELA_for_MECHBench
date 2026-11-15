import numpy as np

class ChaoticModulatedBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial component for global shaping
        poly = np.sum(x**4)
        
        # Trigonometric component for local modulation
        trig = np.sum(np.sin(0.5 * x) * np.cos(0.3 * x))
        
        # Radial basis component for center attraction
        rb = np.sum(np.exp(-0.1 * (x**2)))
        
        # Cross-term interaction to create non-separability
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * np.cos(0.2 * (x[i] + x[j]))
        
        # Chaotic modulation using logistic map behavior
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.exp(-0.02 * np.abs(x[i])) * np.sin(5 * np.pi * x[i])
        
        # Combine all components with different weights
        return 0.6 * poly + 0.3 * trig + 0.2 * rb + 0.1 * cross + 0.15 * chaotic + 0.05 * np.sum(x**6)