import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Polynomial terms with varying degrees and coefficients
        for i in range(self.dim):
            result += (x[i] ** 4) * (i + 1) * 0.1
        
        # Trigonometric components creating multiple local minima
        for i in range(self.dim):
            result += 3 * np.sin(x[i]) * np.cos(2 * x[i]) * (1 + 0.2 * np.sin(3 * x[i]))
        
        # Exponential terms adding steep gradients and sharp changes
        for i in range(self.dim):
            result += 2 * np.exp(-0.5 * (x[i] - 1) ** 2) * np.sin(0.5 * x[i])
        
        # Cross-dimensional interaction terms
        for i in range(self.dim):
            result += 0.8 * x[i] * np.sin(x[(i + 1) % self.dim]) * np.cos(x[(i + 2) % self.dim])
        
        # High-frequency oscillations to increase complexity
        for i in range(self.dim):
            result += 1.5 * np.sin(5 * x[i]) * np.cos(4 * x[(i + 1) % self.dim]) * np.sin(3 * x[(i + 2) % self.dim])
        
        # Add a global scaling factor to control the overall function range
        result *= 1.0 + 0.1 * np.sum(np.abs(x))
        
        return result