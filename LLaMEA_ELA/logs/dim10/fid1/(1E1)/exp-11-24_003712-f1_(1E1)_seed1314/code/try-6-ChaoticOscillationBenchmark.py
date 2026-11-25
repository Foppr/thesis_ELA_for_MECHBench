import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Sinusoidal oscillation term
        oscillation_term = np.sum(np.sin(5.0 * x) ** 2, axis=1)
        
        # Exponential barrier term
        barrier_term = np.sum(np.exp(2.0 * np.abs(x)) * (x**2), axis=1)
        
        # Chaotic component with logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(3.0 * np.pi * x[:, i]) * np.cos(7.0 * np.pi * x[:, i])
        
        # Combine all terms with different weights
        return 0.5 * oscillation_term + 0.3 * barrier_term + 0.2 * chaotic_term