import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Combine logarithmic barrier terms with high-frequency trigonometric peaks
        result = np.sum(np.log(1.0 + x**2 / 25.0)) + 5.0 * np.sum(np.cos(12 * x) * np.sin(18 * x)) + 0.03 * np.sum(x**4)
        
        # Add polynomial conditioning to create varying gradient steepness
        result += 0.15 * np.sum((x**2 + x**3 + x**4) / (1.0 + np.abs(x)))
        
        # Introduce cross-dimensional couplings and chaotic interactions
        for i in range(self.dim):
            for j in range(i+1, self.dim):
                result += 0.02 * np.sin(8 * x[i]) * np.cos(8 * x[j]) * (x[i]**2 + x[j]**2)
        
        return result