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
        f2 = np.sum(np.sin(15 * np.pi * x_norm)**8)
        
        # Exponential barrier terms with modified decay rate to create rugged landscape
        f3 = np.sum(np.exp(-2.0 * x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**4 * np.cos(3 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.5 * np.sum(np.abs(x_norm)**0.5)
        
        return f1 + 0.2 * f2 + 0.15 * f3 + 0.05 * f4 + 0.02 * f5