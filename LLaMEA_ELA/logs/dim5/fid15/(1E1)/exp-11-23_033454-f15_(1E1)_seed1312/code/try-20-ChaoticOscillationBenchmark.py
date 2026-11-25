import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Input dimension must match the function dimension")
        
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Radial basin term - pulls towards origin with varying strength
        radial_term = 0.05 * np.sum(x**2)
        
        # Sinusoidal oscillation terms creating multiple local minima
        sin_term = 0.0
        
        # Use different frequencies for each dimension
        for i in range(self.dim):
            sin_term += np.sin(3.0 * x[i]) * np.cos(2.0 * x[i]) * np.exp(-0.1 * x[i]**2)
            
        # Cross-terms creating complex interactions between dimensions
        cross_term = 0.0
        
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * np.exp(-0.05 * (x[i]**2 + x[j]**2))
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        if self.dim >= 2:
            for i in range(min(3, self.dim)):  # Limit to first few dimensions
                chaotic_term += np.sin(10.0 * x[i]) * np.cos(7.0 * x[(i+1) % self.dim])
        
        # Combine all terms with different weights
        return radial_term - sin_term + cross_term + 0.1 * chaotic_term