import numpy as np

class ChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.logistic_r = 3.97
        
    def f(self, x):
        # Normalize input to [-1, 1] range
        x_norm = x / 5.0
        
        # Initialize chaotic sequence
        chaotic_seq = np.zeros(self.dim)
        for i in range(self.dim):
            if i == 0:
                chaotic_seq[i] = 0.5
            else:
                chaotic_seq[i] = self.logistic_r * chaotic_seq[i-1] * (1 - chaotic_seq[i-1])
        
        # Create coupled chaotic terms
        chaotic_terms = np.zeros(self.dim)
        for i in range(self.dim):
            chaotic_terms[i] = np.sin(10 * np.pi * x_norm[i]) * chaotic_seq[i % len(chaotic_seq)]
        
        # Combine with quadratic and sinusoidal components
        f1 = np.sum(x_norm**2)  # Quadratic basin
        f2 = 0.5 * np.sum(chaotic_terms**2)  # Chaotic interaction
        f3 = 0.1 * np.sum(np.sin(3 * np.pi * x_norm))  # Additional oscillations
        
        # Add coupling between dimensions
        coupling = 0.05 * np.sum((x_norm[1:] - x_norm[:-1])**2)
        
        return f1 + f2 + f3 + coupling