import numpy as np

class MultimodalAttractiveBasin:
    def __init__(self, dim):
        self.dim = dim
        self.bounds = type('Bounds', (), {'lb': np.full(dim, -5.0), 'ub': np.full(dim, 5.0)})()
    
    def f(self, x):
        # Normalize input to [-1, 1] range for better numerical stability
        x_norm = x / 5.0
        
        # Central attractive basin term, significantly shifted and deeper
        basin_term = -2.0 * np.exp(-np.sum((x_norm - 0.3)**2) / (2 * 0.3**2))
        
        # Highly oscillatory sinusoidal component with exponentially decaying amplitudes
        freqs = np.arange(1, self.dim + 1)
        oscillation_term = np.sum(np.sin(freqs * np.pi * x_norm) ** 2 * np.exp(-freqs / self.dim))
        
        # Multimodal nonlinearity with cubic and quintic terms for increased complexity
        multi_term = np.sum(x_norm**5 * np.sin(3 * np.pi * x_norm)**2 + x_norm**3 * np.cos(5 * np.pi * x_norm)**2)
        
        # Strong cross-dimensional coupling with interaction weights decreasing exponentially
        cross_term = 0.7 * np.sum(np.exp(-np.arange(1, self.dim)) * x_norm[:-1] * x_norm[1:])
        
        # Additional deceptive valley term to mislead optimization algorithms
        valley_term = 0.3 * np.sum(np.sin(10 * np.pi * x_norm) ** 4)
        
        # Combine all terms
        return basin_term + oscillation_term + multi_term + cross_term + valley_term