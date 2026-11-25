import numpy as np

class ExponentialSinusoidalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Scale input to [-5, 5] domain
        x = np.array(x)
        
        # Compute exponential decay factor
        decay_factor = np.exp(-np.sum(x**2) / (2 * self.dim))
        
        # Compute sinusoidal terms with varying frequencies
        term1 = np.sum(np.sin(2 * np.pi * x) * np.exp(-0.1 * np.abs(x))) / self.dim
        term2 = np.sum(np.cos(3 * np.pi * x) * np.exp(-0.05 * np.abs(x))) / self.dim
        term3 = np.sum(np.sin(0.5 * np.pi * x) * np.exp(-0.2 * np.abs(x))) / self.dim
        
        # Combine terms with exponential decay
        return decay_factor * (np.sum(x**2) / self.dim + 0.5 * term1 + 0.3 * term2 + 0.2 * term3)