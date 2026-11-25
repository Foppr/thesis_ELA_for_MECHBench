import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Enhanced sinusoidal terms with higher frequencies
        for i in range(self.dim):
            f += 0.5 * np.sin(12 * x[i]) * np.cos(7 * x[(i + 1) % self.dim])
            
        # Non-adjacent dimension interactions with cubic terms
        for i in range(self.dim):
            f += 0.2 * np.sin(6 * x[i]) * np.sin(4 * x[(i + 3) % self.dim]) * np.abs(x[i])
            
        # Modified penalty terms with higher-order polynomials and additional sinusoidal components
        f += 0.05 * np.sum(np.abs(x)**1.5) + 0.02 * np.sum(x**6) + 0.3 * np.sum(np.sin(0.7 * x))
        
        return f