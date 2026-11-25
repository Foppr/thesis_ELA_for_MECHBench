import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin with radial component
        result = np.sum(x**2) * np.exp(-np.sum(x**2) / 50.0)
        
        # Add chaotic oscillations with varying frequencies
        for i in range(self.dim):
            result += 2.0 * np.exp(-0.1 * (x[i] - 1.0)**2) * np.sin(3.0 * x[i]) * np.cos(7.0 * x[i])
        
        # Add radial symmetry with multiple peaks
        r = np.sqrt(np.sum(x**2))
        result += 0.5 * np.sin(5.0 * r) * np.exp(-r / 3.0)
        
        # Add coupling terms with exponential decay
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                dist = np.abs(x[i] - x[j])
                result += 0.3 * np.exp(-dist) * np.sin(2.0 * (x[i] + x[j]))
                
        # Add a small noise term to increase complexity
        result += 0.01 * np.sum(np.sin(10.0 * x))
        
        return result