import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial term creating a basin structure
        radial = np.sum(x**2) * 0.01
        
        # Sinusoidal oscillations with varying frequencies
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Cross-term interactions creating complex landscape
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += (x[i] * x[j]) / (1.0 + np.abs(x[i] - x[j])**2)
        
        # Chaotic component using logistic map-like behavior
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(10.0 * x[i]) * np.cos(7.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Combine all terms with different weights
        result = radial + 0.5 * sin_term + 0.3 * cross_term + 0.2 * chaotic
        
        # Add a small noise term to make it more challenging
        noise = 0.001 * np.sum(np.sin(x * 10.0))
        
        return result + noise