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
        f3 = np.sum(np.exp(-x_norm**2 / 1.5))
        
        # Mixed polynomial and trigonometric term for complex landscape
        f4 = np.sum(x_norm**6 * np.cos(3 * np.pi * x_norm))
        
        # Add a small cubic component for asymmetry
        f5 = 0.15 * np.sum(x_norm**3)
        
        # Additional harmonic term to increase complexity and improve discrimination
        f6 = np.sum(np.sin(5 * x_norm) * np.cos(7 * x_norm))
        
        # Add a quartic term to enhance non-convexity
        f7 = 0.05 * np.sum(x_norm**4)
        
        return 0.4 * f1 + 0.25 * f2 + 0.3 * f3 + 0.1 * f4 + 0.08 * f5 + 0.05 * f6 + 0.07 * f7