import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term for convexity and conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms creating many local minima
        f2 = np.sum(np.sin(10 * np.pi * x_norm)**4)
        
        # Exponential barrier term to encourage boundary exploration
        f3 = np.sum(np.exp(-x_norm**2 / 2.0))
        
        # Mixed polynomial and trigonometric term for complex landscape
        f4 = np.sum(x_norm**4 * np.cos(2 * np.pi * x_norm))
        
        # Add a small cubic component for asymmetry
        f5 = 0.1 * np.sum(x_norm**3)
        
        return 0.5 * f1 + 0.2 * f2 + 0.3 * f3 + 0.1 * f4 + 0.05 * f5