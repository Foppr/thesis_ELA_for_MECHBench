import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with different scales and slight shift
        for i in range(self.dim):
            result += (x[i] ** 2) * (i + 1) + 0.1 * np.sin(0.7 * x[i])
        
        # Add multiple local minima using modified trigonometric terms with phase shifts
        for i in range(self.dim):
            result += 15 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[(i + 1) % self.dim] + 0.5)
        
        # Add a small noise term to increase complexity
        result += 0.15 * np.sum(np.sin(x))
        
        # Introduce a new interaction term with different frequency and amplitude
        for i in range(self.dim):
            result += 10 * np.cos(0.8 * x[i]) * np.sin(0.3 * x[(i + 2) % self.dim] + 0.2)
        
        return result