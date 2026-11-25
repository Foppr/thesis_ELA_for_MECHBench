import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function
        result = 0.0
        for i in range(self.dim):
            # Use a combination of quadratic and trigonometric terms to create complex landscape
            a = 1.0 + i * 0.3
            b = 0.7 + i * 0.15
            result += a * (x[i]**2 - 2 * x[i] * np.sin(x[i])) + b * np.cos(2 * x[i])**2
            
        # Add a global minimum at origin with additional penalty terms
        result += 0.03 * np.sum(x**2)
        
        # Add a small sinusoidal modulation to increase the number of local minima
        result += 0.15 * np.sin(0.3 * np.sum(x))**2
        
        return result