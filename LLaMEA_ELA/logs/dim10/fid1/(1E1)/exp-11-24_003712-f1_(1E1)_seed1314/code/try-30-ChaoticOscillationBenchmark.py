import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Sinusoidal oscillation term
        oscillation_term = np.sum(np.sin(5.0 * x) ** 2, axis=1)
        
        # Exponential barrier terms to create rugged landscape
        barrier_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            # Create exponential barriers at specific points
            barrier = np.exp(-np.sum((x[:, i:i+1] - np.linspace(-4.0, 4.0, 5))**2, axis=1) / 2.0)
            barrier_term += barrier
        
        # Combine terms with different weights and add a quadratic basin
        return 0.3 * oscillation_term + 0.7 * barrier_term + 0.1 * np.sum(x**2, axis=1)