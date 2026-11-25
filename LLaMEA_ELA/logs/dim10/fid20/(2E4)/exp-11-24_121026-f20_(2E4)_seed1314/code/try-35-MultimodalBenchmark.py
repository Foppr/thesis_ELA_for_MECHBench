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
        f2 = np.sum(np.sin(20 * np.pi * x_norm)**8)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**8 * np.cos(7 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.5 * np.sum(np.abs(x_norm)**0.25)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.15 * np.sum(np.sin(25 * x_norm**2) * np.cos(9 * x_norm))
        
        # Cross-term interactions to increase landscape complexity
        f7 = 0.05 * np.sum((x_norm[:-1] + x_norm[1:])**2 * np.sin(10 * np.pi * (x_norm[:-1] - x_norm[1:])))
        
        return f1 + 0.4 * f2 + 0.2 * f3 + 0.1 * f4 + 0.08 * f5 + 0.05 * f6 + 0.03 * f7