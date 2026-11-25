import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        # Sum of quadratic terms with different coefficients and offsets
        result = 0.0
        for i in range(self.dim):
            # Different coefficients for each dimension
            a = 1.0 + i * 0.1
            # Add sinusoidal modulation to create multiple local minima
            result += a * (x[i] - np.sin(x[i]))**2 + 0.1 * np.sin(5 * x[i])**2
        
        # Add a global minimum at origin with additional penalty terms
        result += 0.01 * np.sum(x**2)
        
        return result