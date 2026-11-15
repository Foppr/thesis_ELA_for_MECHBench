import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for added complexity
        self.chaos_seq = np.sin(np.arange(dim) * np.pi / 4.0) * np.exp(-np.arange(dim) * 0.1)
    
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Base quadratic term with varying curvature
        quadratic = np.sum((x_norm ** 2) * (1.0 + 0.2 * np.sin(self.chaos_seq)))
        
        # Chaotic sine modulation with saddle points
        chaotic = 0.0
        for i in range(self.dim):
            chaotic += np.sin(3 * np.pi * x_norm[i]) * np.cos(2 * np.pi * x_norm[i]) * \
                       (1.0 + 0.1 * np.sin(7 * x_norm[i]))
        
        # Add noise component with non-uniform distribution
        noise = np.sum(np.random.laplace(0, 0.5, self.dim) * (1.0 + 0.3 * np.cos(5 * x_norm)))
        
        # Cross-dimensional interaction with chaotic weights
        interaction = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                interaction += (x_norm[i] * x_norm[j]) * np.sin(self.chaos_seq[i] + self.chaos_seq[j])
        
        # Saddle point modifier
        saddle = 0.0
        for i in range(self.dim):
            saddle += (x_norm[i] ** 3) * np.cos(4 * x_norm[i])
        
        return 0.3 * quadratic + 0.4 * chaotic + 0.1 * noise + 0.15 * interaction + 0.05 * saddle