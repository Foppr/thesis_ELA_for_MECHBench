import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Sinusoidal oscillation term
        oscillation_term = np.sum(np.sin(5.0 * x), axis=1)
        
        # Exponential barrier terms to create sharp transitions
        barrier_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            barrier_term += np.exp(2.0 * np.abs(x[:, i]) / 5.0) * np.sin(3.0 * x[:, i])**2
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(10.0 * np.sin(x[:, i])) * np.cos(7.0 * x[:, i])
        
        # Combine all terms with different weights
        result = 0.5 * oscillation_term + 0.3 * barrier_term + 0.2 * chaotic_term
        
        # Add quadratic basin to ensure global minimum at origin
        basin_term = 0.1 * np.sum(x**2, axis=1)
        
        return result + basin_term