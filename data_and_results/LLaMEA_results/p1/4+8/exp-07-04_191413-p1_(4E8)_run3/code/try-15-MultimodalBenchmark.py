import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = np.sum(x**2)
        
        # Add chaotic behavior with exponential decay
        for i in range(self.dim):
            result += np.exp(-0.5 * np.sum(x**2)) * np.sin(3 * x[i]) * np.cos(2 * x[i])
        
        # Add radial symmetry with multiple peaks
        r = np.sqrt(np.sum(x**2))
        result += 0.5 * np.exp(-r**2 / 10.0) * np.sin(5 * r) * np.cos(3 * r)
        
        # Add high-frequency oscillations
        for i in range(self.dim):
            result += 0.3 * np.sin(10 * x[i]) * np.cos(7 * x[i]) * np.exp(-0.1 * x[i]**2)
        
        # Add coupling terms between dimensions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.1 * np.exp(-0.5 * (x[i]**2 + x[j]**2)) * np.sin(2 * x[i] * x[j])
        
        # Add a small noise-like component
        result += 0.02 * np.sum(np.sin(15 * x) + np.cos(12 * x))
        
        return result