import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency sinusoidal terms with multiple local minima
        f2 = np.sum(np.sin(30 * np.pi * x_norm)**6)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**10 * np.cos(9 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.7 * np.sum(np.abs(x_norm)**0.3)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.2 * np.sum(np.sin(30 * x_norm**2) * np.cos(11 * x_norm))
        
        # Cross-term interactions to increase landscape complexity
        f7 = 0.08 * np.sum((x_norm[:-1] + x_norm[1:])**3 * np.sin(15 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        # Additional quartic polynomial interaction term
        f8 = 0.02 * np.sum((x_norm**2 + x_norm[::-1]**2)**2)
        
        return f1 + 0.5 * f2 + 0.25 * f3 + 0.15 * f4 + 0.1 * f5 + 0.06 * f6 + 0.04 * f7 + 0.01 * f8