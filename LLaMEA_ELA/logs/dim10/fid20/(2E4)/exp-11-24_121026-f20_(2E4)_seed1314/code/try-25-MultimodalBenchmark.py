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
        f2 = np.sum(np.sin(15 * np.pi * x_norm)**6)
        
        # Exponential barrier term to encourage boundary exploration
        f3 = np.sum(np.exp(-x_norm**2 / 0.5))
        
        # Mixed polynomial and trigonometric term for complex landscape
        f4 = np.sum(x_norm**6 * np.cos(3 * np.pi * x_norm))
        
        # Add a highly non-linear component with multiple peaks
        f5 = np.sum(np.sin(20 * x_norm) * np.exp(-x_norm**2))
        
        # Add a quartic interaction term between dimensions
        f6 = np.sum((x_norm[:-1] - x_norm[1:])**4)
        
        # Add a strongly asymmetric cubic component
        f7 = 0.2 * np.sum(np.abs(x_norm)**3)
        
        return 0.3 * f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.05 * f5 + 0.03 * f6 + 0.02 * f7