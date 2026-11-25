import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add exponentially decaying sinusoidal terms with long-range correlations
        for i in range(self.dim):
            decay_factor = np.exp(-0.1 * i)
            f += decay_factor * np.sin(5 * x[i]) * np.cos(3 * x[(i + 1) % self.dim])
            
        # Add higher frequency sinusoids with amplitude modulation
        for i in range(self.dim):
            f += 0.3 * np.sin(10 * x[i]) * np.exp(-0.05 * np.abs(x[i]))
            
        # Add interaction terms between all pairs of dimensions with distance-dependent weights
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = 1.0 / (1.0 + np.abs(i - j))
                f += weight * np.sin(x[i]) * np.cos(x[j])
                
        # Add a global minimum at origin with modified penalty terms
        f += 0.01 * np.sum(np.abs(x)) + 0.002 * np.sum(x**4)
        
        return f