import numpy as np

class MultiModalChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Periodic sinusoidal wells creating multiple local minima
        f1 = np.sum(np.sin(3.0 * x) ** 2 + np.cos(2.0 * x) ** 2)
        
        # Exponential decay barriers between wells
        f2 = np.sum(np.exp(-0.5 * (x - 1.0)**2) + np.exp(-0.5 * (x + 1.0)**2))
        
        # Cross-dimensional coupling with varying strength
        f3 = 0.5 * np.sum((x[:-1] - x[1:]) ** 2 * np.sin(5.0 * x[:-1]))
        
        # Multi-scale periodic structure with diminishing amplitude
        f4 = 0.3 * np.sum(np.sin(10.0 * x) * np.exp(-0.1 * np.abs(x)))
        
        # Chaotic modulation using logistic map-like behavior
        f5 = 0.2 * np.sum(np.sin(np.pi * x * np.cos(x)) ** 2)
        
        # Asymmetric landscape with different curvature in positive/negative directions
        f6 = 0.1 * np.sum(np.where(x >= 0, x**3, -x**3))
        
        # Interaction terms that create complex valleys and ridges
        f7 = 0.15 * np.sum(np.sin(2.0 * x[:-2]) * np.cos(3.0 * x[1:-1]) * np.sin(4.0 * x[2:]))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7