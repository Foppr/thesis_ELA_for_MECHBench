import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Global minimum at origin
        result = 0.0
        
        # Sum of quadratic terms with adaptive scaling
        for i in range(self.dim):
            scale = (i + 1) * 0.5 + 1.0
            result += scale * (x[i] ** 2)
        
        # Add multiple local minima using coupled trigonometric terms
        for i in range(self.dim):
            j = (i + 1) % self.dim
            result += 15 * np.sin(0.7 * x[i]) * np.cos(0.4 * x[j]) * np.exp(-0.1 * (x[i]**2 + x[j]**2))
        
        # Add higher-order polynomial interactions for increased complexity
        for i in range(self.dim):
            result += 5 * (x[i] ** 4) / (1 + np.abs(x[i]))
        
        # Add cross-dimensional coupling with sine waves
        sum_x = np.sum(x)
        result += 8 * np.sin(0.3 * sum_x) * np.cos(0.2 * sum_x)
        
        # Add small random noise to increase robustness
        noise = np.random.normal(0, 0.01)
        result += noise
        
        return result