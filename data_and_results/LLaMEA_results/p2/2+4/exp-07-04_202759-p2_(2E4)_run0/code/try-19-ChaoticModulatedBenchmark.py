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
        trig = np.sum(np.sin(0.7 * x) * np.cos(0.4 * x))
        
        # Radial basis component for center attraction
        rb = np.sum(np.exp(-0.05 * (x**2)))
        
        # Cross-term interaction to create non-separability
        cross = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross += np.sin(x[i] * x[j]) * np.cos(0.15 * (x[i] + x[j]))
        
        # Chaotic modulation using logistic map behavior with enhanced nonlinearity
        chaotic = 0
        for i in range(self.dim):
            chaotic += np.exp(-0.01 * np.abs(x[i])) * np.sin(7 * np.pi * x[i]) * np.cos(0.3 * x[i])
        
        # Additional harmonic modulation for increased complexity
        harmonic = np.sum(np.sin(0.2 * x) * np.cos(0.6 * x) * np.sin(0.8 * x))
        
        # Combine all components with different weights
        return 0.5 * poly + 0.25 * trig + 0.15 * rb + 0.1 * cross + 0.1 * chaotic + 0.05 * harmonic + 0.02 * np.sum(x**6)