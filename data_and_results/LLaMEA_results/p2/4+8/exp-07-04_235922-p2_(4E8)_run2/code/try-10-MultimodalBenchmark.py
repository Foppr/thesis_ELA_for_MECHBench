import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Enhanced sinusoidal perturbations with varying frequencies
        f2 = 0.2 * np.sum(np.sin(3.0 * x) * np.cos(7.0 * x) * np.exp(-0.1 * x**2))
        
        # Additional cosine modulation to create more complex landscape
        f3 = 0.15 * np.sum(np.cos(4.0 * x) * np.sin(9.0 * x) * np.exp(-0.05 * x**2))
        
        # Add a multi-scale exponential decay term
        f4 = 0.05 * np.sum(np.exp(-0.5 * (x**2)) * np.sin(2.0 * x) * np.cos(6.0 * x))
        
        # Combine all components with adaptive weights
        result = f1 + f2 + f3 + f4
        
        return result