import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
    
    def f(self, x):
        # Normalize input to [-1, 1] range for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms creating dense local minima
        f2 = np.sum(np.sin(15 * np.pi * x_norm) ** 2)
        
        # Exponentially increasing frequency terms for complexity
        f3 = np.sum(np.sin(2**(np.arange(1, self.dim + 1) * 1.5) * np.pi * x_norm) ** 2)
        
        # Mixed polynomial terms for non-convexity and varied curvature
        f4 = np.sum(x_norm**4 + 0.3 * x_norm**6)
        
        # Cross-terms to increase dimensionality interaction with chaotic coupling
        f5 = np.sum(np.sin(x_norm[:-1] * x_norm[1:] * np.sin(5 * x_norm[:-1])) ** 2)
        
        # Add a chaotic component that scales with dimensionality
        chaotic_term = np.sum(np.sin(np.exp(x_norm) * np.pi) ** 2)
        
        # Combine all terms with varying weights
        return f1 + 0.6 * f2 + 0.4 * f3 + 0.08 * f4 + 0.25 * f5 + 0.1 * chaotic_term