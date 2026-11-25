import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # High-frequency trigonometric peaks with chaotic interactions
        result = np.sum(np.sin(20 * np.pi * x) * np.cos(15 * np.pi * x)) + np.sum(np.sin(30 * x**2) * np.cos(25 * x**2))
        
        # Logarithmic barrier terms to create narrow minima
        result += np.sum(np.log(1.0 + 0.1 * x**2 / 25.0)) + np.sum(np.log(1.0 + 0.05 * x**4 / 625.0))
        
        # Cross-dimensional couplings and adaptive polynomial penalties
        cross_dim = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                cross_dim += np.sin(x[i] * x[j]) * np.cos(0.5 * (x[i]**2 + x[j]**2))
        
        result += 0.5 * cross_dim + 0.02 * np.sum((x**3 + x**5) / (1.0 + np.abs(x)))
        
        # Add chaotic sine-cosine interactions for increased complexity
        result += 2.0 * np.sum(np.sin(np.pi * x) * np.cos(2 * np.pi * x) * np.sin(3 * np.pi * x))
        
        return result