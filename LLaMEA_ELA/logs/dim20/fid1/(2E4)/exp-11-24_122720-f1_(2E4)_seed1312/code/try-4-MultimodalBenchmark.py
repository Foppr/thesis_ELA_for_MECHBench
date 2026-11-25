import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term
        f1 = np.sum(x_norm**2)
        
        # High-frequency sine components with exponential growth
        frequencies = np.exp(np.arange(1, self.dim + 1) * 0.5)
        f2 = np.sum(np.sin(frequencies * x_norm))
        
        # Polynomial interaction terms
        f3 = np.sum(x_norm**4)
        
        # Chaotic cross-terms using sine of products
        cross_terms = np.array([np.sin(np.prod(x_norm[:i+1])) for i in range(self.dim)])
        f4 = np.sum(cross_terms)
        
        # Exponentially decaying weights to create complex landscape
        weights = np.exp(-np.arange(1, self.dim + 1) * 0.3)
        f5 = np.sum(weights * np.cos(3 * np.pi * x_norm))
        
        # Combine all terms with varying influence
        return 0.05 * f1 + 0.1 * f2 + 0.02 * f3 + 0.08 * f4 + 0.03 * f5 + 2.0