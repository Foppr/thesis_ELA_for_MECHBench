import numpy as np

class RuggedHybridBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Polynomial basin term with varying degrees
        polynomial = np.sum(0.5 * x**2 + 0.1 * x**3 + 0.02 * x**4)
        
        # Trigonometric oscillations with varying frequencies and phases
        trigonometric = 0.0
        for i in range(self.dim):
            trigonometric += np.sin(3 * x[i]) * np.cos(2 * x[(i + 1) % self.dim])
            trigonometric += 0.5 * np.sin(5 * x[i]) * np.exp(-0.5 * x[i]**2)
            trigonometric += 0.3 * np.cos(4 * x[i]) * np.sin(6 * x[(i + 2) % self.dim])
        
        # Exponential interaction terms with asymmetric weights
        exponential = 0.0
        for i in range(self.dim):
            exponential += 0.4 * np.exp(-0.1 * (x[i] - 1)**2) * np.sin(3 * x[(i + 1) % self.dim])
            exponential += 0.2 * np.exp(-0.2 * (x[i] + 2)**2) * np.cos(5 * x[(i + 2) % self.dim])
        
        # Rugged terrain with step-like discontinuities and local perturbations
        rugged = 0.0
        for i in range(self.dim):
            rugged += 0.3 * np.floor(np.abs(x[i]) / 1.5) * np.sin(2 * x[i])
            rugged += 0.1 * np.random.rand() * np.cos(10 * x[i])
        
        # Asymmetric cross-dimensional interactions
        cross_dim = 0.0
        for i in range(self.dim):
            cross_dim += 0.2 * x[i] * np.sin(3 * x[(i + 1) % self.dim]) * np.exp(-0.1 * x[i]**2)
            cross_dim += 0.15 * x[i]**2 * np.cos(4 * x[(i + 2) % self.dim])
        
        # Final fitness value with weighted components
        return 0.6 * polynomial + 1.2 * trigonometric + 1.0 * exponential + 0.8 * rugged + 0.9 * cross_dim