import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Quadratic term with increasing weight per dimension
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1)
        
        # Sine-based oscillations with exponentially decaying interaction weights
        for i in range(self.dim):
            weight = np.exp(-0.1 * i)
            result += weight * np.sin(2.0 * x[i]) * np.cos(1.5 * x[(i + 1) % self.dim])
        
        # Higher frequency components with dimension-specific scaling
        for i in range(self.dim):
            result += 3.0 * np.sin(5.0 * x[i]) * (1 + 0.2 * np.cos(3.0 * x[(i + 2) % self.dim]))
        
        # Cross-dimension interaction terms with exponential decay
        for i in range(self.dim):
            result += 0.7 * x[i] * np.sin(0.8 * x[(i + 1) % self.dim]) * np.exp(-0.05 * i)
        
        # Add noise-like term to increase complexity
        result += 0.2 * np.sum(np.sin(0.5 * x))
        
        return result