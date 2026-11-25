import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f = np.sum(x**2)
        
        # Add multiple local minima using enhanced sinusoidal terms with modified frequencies
        for i in range(self.dim):
            f += 0.4 * np.sin(9 * x[i]) * np.cos(6 * x[(i + 1) % self.dim])
            
        # Add additional interaction terms between non-adjacent dimensions with different coefficients
        for i in range(self.dim):
            f += 0.2 * np.sin(5 * x[i]) * np.sin(4 * x[(i + 2) % self.dim])
            
        # Add shifted local minima and modified penalty terms
        f += 0.05 * np.sum(np.abs(x)) + 0.02 * np.sum(x**4) + 0.25 * np.sum(np.sin(0.6 * x))
        
        # Add cross-dimensional interaction with higher frequency sinusoids
        for i in range(self.dim):
            f += 0.1 * np.cos(7 * x[i]) * np.sin(3 * x[(i + 3) % self.dim])
            
        return f