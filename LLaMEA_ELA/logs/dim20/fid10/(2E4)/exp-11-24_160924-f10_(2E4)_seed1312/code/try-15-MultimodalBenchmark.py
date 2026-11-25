import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Compute the multimodal function with enhanced complexity
        result = 0.0
        for i in range(self.dim):
            # Use varying coefficients and add higher frequency sinusoidal terms
            a = 1.0 + i * 0.2
            b = 0.5 + i * 0.1
            # Add multiple sinusoidal components to increase landscape complexity
            result += a * (x[i]**2 - 2 * x[i] * np.sin(x[i]))**2 + \
                     b * np.sin(3 * x[i])**2 + \
                     0.3 * np.sin(7 * x[i])**4
        
        # Add global minimum with enhanced penalty terms
        result += 0.02 * np.sum(x**2) + 0.1 * np.sum(np.abs(x))**1.5
        
        return result