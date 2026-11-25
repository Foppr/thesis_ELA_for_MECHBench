import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency trigonometric terms creating multiple local minima
        f2 = np.sum(np.sin(30 * x_norm)**4)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**5 * np.cos(7 * x_norm))
        
        # Global repulsion term to prevent easy convergence
        f5 = 0.4 * np.sum(np.abs(x_norm)**0.25)
        
        # Chaotic logistic-like component with adaptive frequency
        f6 = 0.3 * np.sum(np.sin(np.pi * x_norm * np.sin(18 * x_norm))**6)
        
        # Fourth-order polynomial with random coefficients for extra ruggedness
        f7 = 0.05 * np.sum((x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2 + 0.2 * x_norm)**2)
        
        # Additional high-frequency modulation term
        f8 = 0.25 * np.sum(np.sin(22 * x_norm * np.cos(9 * x_norm))**5)
        
        # Adaptive scaling factor based on dimensionality
        adaptive_scale = 1.0 + 0.1 * np.log(self.dim + 1)
        
        return adaptive_scale * (f1 + 0.4 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.08 * f6 + 0.05 * f7 + 0.07 * f8)