import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with polynomial base
        result = np.sum(x**4) / 100.0
        
        # Add trigonometric oscillations with varying frequencies and amplitudes
        for i in range(self.dim):
            result += 3.0 * np.sin(2.0 * x[i]) * np.cos(5.0 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add logarithmic barrier terms to create complex terrain near boundaries
        log_barrier = 0.0
        for i in range(self.dim):
            log_barrier += 1.0 / (1.0 + np.exp(-x[i] + 5.0)) + 1.0 / (1.0 + np.exp(x[i] + 5.0))
        result += 2.0 * log_barrier
        
        # Add coupling terms with sinusoidal decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.sqrt((x[i] - x[j])**2 + 0.1)
                result += 1.5 * np.sin(3.0 * dist) * np.exp(-dist / 2.0)
        
        # Add radial component with multiple peaks
        r = np.sqrt(np.sum(x**2))
        result += 1.0 * np.sin(10.0 * r) * np.exp(-r / 4.0)
        
        # Add a small noise term to increase complexity
        result += 0.05 * np.sum(np.cos(15.0 * x))
        
        return result