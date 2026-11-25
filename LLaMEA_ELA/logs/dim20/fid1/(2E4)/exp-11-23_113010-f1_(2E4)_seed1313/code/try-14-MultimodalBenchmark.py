import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        
    def f(self, x):
        # Normalize input to [-1, 1] range for better conditioning
        x_norm = x / 5.0
        
        # Sum of quadratic terms with different scales
        term1 = np.sum(x_norm**2)
        
        # Sum of sine terms with different frequencies and amplitudes
        term2 = np.sum(np.sin(5 * np.pi * x_norm)**2) + 0.5 * np.sum(np.sin(3 * np.pi * x_norm)**2)
        
        # Product of cosines for additional complexity with varying frequencies
        term3 = np.prod(np.cos(2 * np.pi * x_norm)) * np.prod(np.cos(4 * np.pi * x_norm))
        
        # Additional interaction term between all dimensions using exponential decay
        term4 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Cross-terms with interaction between pairs of dimensions
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_norm[i] - x_norm[j])**2 * np.sin(np.pi * (x_norm[i] + x_norm[j]))
        term5 = interaction * 0.3
        
        # Add a small noise component to create more complex landscape
        noise = 0.01 * np.random.random()
        
        return term1 + 0.8 * term2 - 0.5 * term3 + 0.2 * term4 + term5 + noise