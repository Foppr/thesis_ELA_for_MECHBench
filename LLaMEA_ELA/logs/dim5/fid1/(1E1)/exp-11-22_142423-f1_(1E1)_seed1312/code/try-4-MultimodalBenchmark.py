import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Enhanced sinusoidal interactions with higher frequency components
        for i in range(self.dim):
            f += 0.3 * np.sin(10 * x[i]) * np.cos(5 * x[(i + 1) % self.dim]) * np.sin(3 * x[(i + 2) % self.dim])
            
        # Add multi-scale interaction terms
        for i in range(self.dim):
            f += 0.15 * np.sin(6 * x[i]) * np.cos(8 * x[(i + 3) % self.dim]) + 0.1 * np.cos(9 * x[i]) * np.sin(7 * x[(i + 4) % self.dim])
            
        # Introduce complex penalty terms with exponential and polynomial components
        f += 0.03 * np.sum(np.exp(0.5 * np.abs(x))) + 0.01 * np.sum(x**6) + 0.02 * np.sum(np.abs(x)**1.5)
        
        # Add a secondary global minimum to increase difficulty
        f += 0.05 * np.sum((x - 1.0)**4) + 0.05 * np.sum((x + 1.0)**4)
        
        return f