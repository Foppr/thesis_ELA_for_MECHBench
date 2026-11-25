import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Combine logarithmic barrier terms with high-frequency trigonometric peaks
        result = np.sum(np.log(1.0 + x**2 / 25.0)) + 3.0 * np.sum(np.cos(10 * x) * np.sin(15 * x)) + 0.05 * np.sum(x**4)
        
        # Add polynomial conditioning to create varying gradient steepness
        result += 0.1 * np.sum((x**2 + x**3 + x**4) / (1.0 + np.abs(x)))
        
        return result