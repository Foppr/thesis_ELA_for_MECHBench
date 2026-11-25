import numpy as np

class ChaoticSaddleBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute chaotic sequence for varying complexity
        self.chaos_seq = np.sin(np.arange(dim) * np.pi / 4.0)
    
    def f(self, x):
        # Clamp input to domain [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic gradient modulation
        chaotic_mod = np.sum(self.chaos_seq * np.sin(x))
        
        # Saddle-node potential wells with varying depths
        saddle_potential = 0.0
        for i in range(self.dim):
            xi = x[i]
            # Quadratic + cubic term creating asymmetric saddle
            saddle_potential += (xi**2 - 1.0)**2 + 0.3 * xi**3
        
        # Power-law correlated noise component
        noise = 0.0
        for i in range(self.dim):
            # Simulate long-range correlations using weighted sum
            weight = 1.0 / (1.0 + np.abs(i - self.dim//2))
            noise += weight * np.sin(5.0 * xi) * np.cos(2.0 * xi)
        
        # Cross-dimensional coupling with exponential decay
        coupling = 0.0
        for i in range(self.dim-1):
            coupling += np.exp(-0.1 * np.abs(x[i] - x[i+1])) * (x[i]**2 + x[i+1]**2)
        
        # Global scaling factor based on dimensionality
        scale = 1.0 + 0.1 * self.dim
        
        return scale * (saddle_potential + coupling + noise + chaotic_mod**2)