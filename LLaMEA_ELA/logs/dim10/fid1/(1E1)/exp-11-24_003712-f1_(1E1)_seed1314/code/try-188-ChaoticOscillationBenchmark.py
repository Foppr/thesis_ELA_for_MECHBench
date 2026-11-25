import numpy as np

class ChaoticOscillationBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
        
        # Central repulsive force term
        center_distance = np.sum(x**2, axis=1)
        repulsion_term = 2.0 * np.exp(-center_distance / 10.0)
        
        # Sinusoidal oscillation terms
        oscillation_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            oscillation_term += np.sin(x[:, i] * (i + 1) * 2.0) * np.cos(x[:, i] * (i + 1) * 1.5)
        
        # Chaotic component with exponential growth
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(x[:, i] * np.pi * (i + 1)) * np.cos(x[:, i] * np.pi * (i + 1))
        
        # Combine all terms with different weights
        return 0.5 * center_distance + 0.3 * oscillation_term + 0.2 * chaotic_term + repulsion_term