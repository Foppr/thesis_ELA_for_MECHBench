import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        quadratic = np.sum(x**2)
        
        # Chaotic sinusoidal modulation with varying frequencies
        chaotic = 0
        for i in range(self.dim):
            freq = 10 + 5 * np.sin(x[i] * 0.5)
            chaotic += np.sin(freq * x[i]) * np.cos(freq * x[i] * 1.3) * np.exp(-0.1 * x[i]**2)
        
        # Multi-scale interference pattern
        interference = 0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                interference += np.sin(20 * dist) * np.cos(15 * dist) * np.exp(-0.5 * dist**2)
        
        # Implicit constraint term (creates sharp ridges and valleys)
        constraint = 0
        for i in range(self.dim):
            constraint += (x[i] - np.sin(x[i]))**2
        
        # Gradient-based chaotic component
        gradient = 0
        for i in range(self.dim):
            grad_term = np.cos(x[i]) * np.sin(x[i]) * np.exp(-0.2 * x[i]**2)
            gradient += grad_term * (1 + 0.3 * np.sin(5 * x[i]))
        
        # Combined with exponential decay and multipliers
        return 0.4 * quadratic + 0.3 * chaotic + 0.2 * interference + 0.1 * constraint + 0.05 * gradient