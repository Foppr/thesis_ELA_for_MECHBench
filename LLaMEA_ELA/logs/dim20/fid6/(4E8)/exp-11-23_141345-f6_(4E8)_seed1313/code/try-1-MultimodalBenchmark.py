import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_normalized = x / 5.0
        
        # Sum of quadratic terms with different scales
        f1 = np.sum(x_normalized**2)
        
        # Sum of sine terms with different frequencies
        f2 = np.sum(np.sin(5 * np.pi * x_normalized)**2)
        
        # Product of cosine terms creating complex landscape
        f3 = np.prod(np.cos(2 * np.pi * x_normalized) + 1)
        
        # Add noise term to make it non-convex and challenging
        noise = 0.1 * np.random.random()
        
        return f1 + 0.5 * f2 + 0.3 * f3 + noise