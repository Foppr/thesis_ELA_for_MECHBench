import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x) != self.dim:
            raise ValueError("Dimension mismatch")
            
        # Scale input to [-pi, pi] for sinusoidal components
        scaled_x = x * np.pi / 5.0
        
        # Sinusoidal oscillation term - creates many local minima
        sin_term = np.sum(np.sin(scaled_x) * np.cos(3 * scaled_x))
        
        # Exponential barrier term - creates sharp transitions and plateaus
        barrier_term = 0.0
        for i in range(self.dim):
            barrier_term += np.exp(-np.abs(x[i]) / 2.0) * np.sin(x[i])**2
        
        # Quadratic basin term - encourages convergence to origin
        basin_term = 0.1 * np.sum(x**2)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = 0.0
        for i in range(self.dim):
            if i > 0:
                chaotic_term += np.sin(x[i-1] * x[i]) * 0.5
            
        # Combine all terms with different weights
        result = -sin_term + barrier_term + basin_term + chaotic_term
        
        # Add small random noise to make it non-trivial
        noise = 0.01 * np.random.rand()
        
        return result + noise