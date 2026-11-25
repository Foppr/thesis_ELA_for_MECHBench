import numpy as np

class ChaoticRuggedBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Sinusoidal oscillation term
        sin_term = np.sum(np.sin(5.0 * x), axis=1)
        
        # Exponential barrier term to create ruggedness
        barrier_term = np.sum(np.exp(2.0 * np.abs(x)) - 1.0, axis=1)
        
        # Chaotic component using logistic map-like behavior
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(3.0 * x[:, i] * np.pi) * np.cos(2.0 * x[:, i] * np.pi)
        
        # Combine all terms with different weights
        return 0.5 * sin_term + 0.3 * barrier_term + 0.2 * chaotic_term