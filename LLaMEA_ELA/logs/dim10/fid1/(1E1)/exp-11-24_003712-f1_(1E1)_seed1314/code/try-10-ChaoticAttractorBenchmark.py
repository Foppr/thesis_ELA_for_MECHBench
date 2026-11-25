import numpy as np

class ChaoticAttractorBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.center = np.zeros(dim)
        
    def f(self, x):
        if len(x.shape) == 1:
            x = x.reshape(1, -1)
            
        # Central attractor term
        central_term = 0.5 * np.sum((x - self.center)**2, axis=1)
        
        # Chaotic sinusoidal terms
        chaotic_term = np.zeros(x.shape[0])
        for i in range(self.dim):
            chaotic_term += np.sin(x[:, i]) * np.cos(2 * x[:, i]) * np.sin(3 * x[:, i])
            
        # Add noise component
        noise_term = 0.1 * np.sum(np.sin(5 * x), axis=1)
        
        # Combine terms with different weights
        return central_term + 0.3 * chaotic_term + 0.2 * noise_term