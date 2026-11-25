import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Chaotic sine-cosine interactions with adaptive penalties
        result = np.sum(np.exp(-x**2 / 3.0) * np.sin(7 * x) * np.cos(4 * x)) + \
                 np.sum(np.sin(12 * x) * np.cos(18 * x) * np.exp(-x**2 / 6.0)) + \
                 np.sum((x**5 + x**4 - x**3) * np.sin(3 * x) * np.cos(5 * x)) + \
                 0.07 * np.sum(np.sin(x) * np.cos(x) * (x**7 + x**6))
        
        # Cross-dimensional coupling terms with modified interaction strength
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.15 * np.sin(x[i] * x[j]) * np.exp(-(x[i]**2 + x[j]**2) / 8.0)
        
        return result