import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x**2)
        
        # Add multiple local minima using sinusoidal terms with higher frequency and amplitude
        f2 = 0.2 * np.sum(np.sin(8.0 * x) * np.exp(-0.15 * x**2))
        
        # Add a global minimum at origin with additional complexity through cosine terms
        f3 = 0.02 * np.sum(np.cos(15.0 * x) * np.exp(-0.08 * x**2))
        
        # Add interaction terms between dimensions to increase complexity
        f4 = 0.05 * np.sum(x[:-1] * x[1:] * np.sin(3.0 * x[:-1] + 2.0 * x[1:]))
        
        # Add a small shift to the landscape to make convergence more challenging
        shift = 0.5
        f5 = 0.1 * np.sum((x - shift)**2)
        
        # Combine all terms
        return f1 + f2 + f3 + f4 + f5