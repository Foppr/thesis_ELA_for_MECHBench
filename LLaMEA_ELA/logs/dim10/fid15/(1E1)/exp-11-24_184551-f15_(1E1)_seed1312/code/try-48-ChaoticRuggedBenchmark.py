import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Ensure all dimensions are within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sinusoidal oscillation term - creates many local minima
        sin_term = 0.0
        for i in range(self.dim):
            sin_term += np.sin(5.0 * x[i]) * np.cos(3.0 * x[i])
        
        # Exponential barrier terms - create sharp transitions and ridges
        barrier_term = 0.0
        for i in range(self.dim):
            # Create barriers at boundaries
            barrier_term += np.exp(-((x[i] - 5.0)**2) / 2.0) + np.exp(-((x[i] + 5.0)**2) / 2.0)
            
        # Cross-term interaction - couples dimensions to create complex landscape
        cross_term = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_term += np.sin(x[i] * x[j]) * 0.1
        
        # Quadratic basin term - encourages convergence but with chaotic modulation
        basin_term = 0.0
        for i in range(self.dim):
            basin_term += (x[i]**2) * (1.0 + 0.1 * np.sin(10.0 * x[i]))
        
        # Combine all terms with different weights
        result = 2.0 * sin_term - 0.5 * barrier_term + cross_term + 0.3 * basin_term
        
        # Add small chaotic noise to make it non-reproducible
        noise = np.sum(np.sin(x * 13.0) * 0.001)
        
        return result + noise