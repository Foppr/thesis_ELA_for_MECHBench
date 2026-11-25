import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-cosine interactions with adaptive penalties
        result = np.sum(np.exp(-x**2 / 2.0) * np.sin(5 * x) * np.cos(3 * x)) + \
                 np.sum(np.sin(10 * x) * np.cos(15 * x) * np.exp(-x**2 / 5.0)) + \
                 np.sum((x**4 + x**3 - x**2) * np.sin(2 * x) * np.cos(4 * x)) + \
                 0.05 * np.sum(np.sin(x) * np.cos(x) * (x**6 + x**5))
        
        # Cross-dimensional coupling terms
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.sin(x[i] * x[j]) * np.exp(-(x[i]**2 + x[j]**2) / 10.0)
        
        return result