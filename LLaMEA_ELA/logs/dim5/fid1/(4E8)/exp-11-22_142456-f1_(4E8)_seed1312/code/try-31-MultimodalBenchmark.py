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
        
        # Add multiple local minima using modified trigonometric terms with phase shifts and cross-dimensional coupling
        for i in range(self.dim):
            result += 15 * np.sin(0.6 * x[i]) * np.cos(0.4 * x[(i + 1) % self.dim] + 0.5) * (1 + 0.1 * np.sin(0.3 * x[i]))
        
        # Add a small noise term to increase complexity with cross-dimensional interactions
        result += 0.15 * np.sum(np.sin(x) * np.cos(0.2 * x))
        
        # Add a higher-order polynomial term for increased landscape complexity
        for i in range(self.dim):
            result += 0.05 * (x[i] ** 4) * np.cos(0.5 * x[(i + 2) % self.dim])
        
        return result