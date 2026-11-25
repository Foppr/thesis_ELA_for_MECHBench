import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Cubic polynomial terms for sharper basins
        polynomial = np.sum(x**3) + 0.05 * np.sum(x**6)
        
        # Exponentially decaying sinusoidal oscillations with varying frequencies
        freqs = np.arange(1, self.dim + 1)
        sinusoidal = np.sum(np.sin(freqs * x) * np.exp(-0.2 * np.abs(x)))
        
        # Long-range interactions via exponentially weighted cross-terms
        cross_terms = 0.0
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                weight = np.exp(-0.1 * (i - j)**2)
                cross_terms += weight * x[i] * x[j]
        
        # Add a global trap term to increase difficulty
        trap = 10.0 * np.exp(-0.5 * np.sum((x - 1.0)**2))
        
        return polynomial + sinusoidal + cross_terms + trap