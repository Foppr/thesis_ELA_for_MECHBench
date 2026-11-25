import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Enhanced sinusoidal terms with varying frequencies and amplitudes
        for i in range(self.dim):
            f += 0.3 * np.sin(5 * x[i]) * np.cos(3 * x[(i + 1) % self.dim]) * np.sin(2 * x[(i + 2) % self.dim])
            
        # Add higher-order interaction terms
        for i in range(self.dim):
            f += 0.15 * np.sin(4 * x[i]) * np.cos(6 * x[(i + 3) % self.dim]) * np.sin(3 * x[(i + 1) % self.dim])
            
        # Add complex polynomial interactions
        for i in range(self.dim):
            f += 0.08 * (x[i]**3) * np.cos(2 * x[(i + 1) % self.dim]) * np.sin(4 * x[(i + 2) % self.dim])
            
        # Adaptive penalty terms that scale with dimensionality
        f += 0.015 * np.sum(np.abs(x)**1.5) + 0.003 * np.sum(np.abs(x)**3.5)
        
        # Add a global minimum at origin with enhanced penalty terms
        f += 0.02 * np.sum(np.abs(x)) + 0.005 * np.sum(x**4)
        
        return f