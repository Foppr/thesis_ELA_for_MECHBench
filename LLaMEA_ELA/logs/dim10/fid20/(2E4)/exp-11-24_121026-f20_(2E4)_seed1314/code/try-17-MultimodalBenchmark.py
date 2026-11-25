import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term for conditioning and convexity
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms creating many local minima
        f2 = np.sum(np.sin(15 * np.pi * x_norm)**6)
        
        # Exponential barrier term to encourage boundary exploration
        f3 = np.sum(np.exp(-x_norm**2 / 0.5))
        
        # Mixed polynomial and trigonometric term for complex landscape
        f4 = np.sum(x_norm**6 * np.cos(3 * np.pi * x_norm))
        
        # Add a quartic component for asymmetry and increased complexity
        f5 = 0.15 * np.sum(x_norm**4)
        
        # Add a cross-term interaction to increase dimensionality coupling
        f6 = 0.05 * np.sum(np.sin(x_norm[:-1] + x_norm[1:]) ** 2)
        
        return 0.4 * f1 + 0.3 * f2 + 0.2 * f3 + 0.05 * f4 + 0.05 * f5 + 0.05 * f6