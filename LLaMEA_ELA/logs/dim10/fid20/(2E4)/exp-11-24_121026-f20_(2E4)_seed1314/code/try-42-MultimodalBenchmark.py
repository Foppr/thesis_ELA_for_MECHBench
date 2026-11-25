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
        f2 = np.sum(np.sin(25 * np.pi * x_norm)**6)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**5 * np.cos(8 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.3 * np.sum(np.abs(x_norm)**0.3)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.2 * np.sum(np.sin(30 * x_norm**2) * np.cos(10 * x_norm))
        
        # Add a new chaotic term with logistic map-like behavior
        f7 = 0.25 * np.sum(np.sin(np.pi * x_norm * np.sin(12 * x_norm))**3)
        
        # Add a fourth-order polynomial with random coefficients for extra ruggedness
        f8 = 0.08 * np.sum((x_norm**4 + 0.4 * x_norm**3 - 0.2 * x_norm**2 + 0.15 * x_norm)**2)
        
        # Add a fifth-order polynomial term with varying coefficients for more complexity
        f9 = 0.1 * np.sum((x_norm**5 - 0.3 * x_norm**4 + 0.2 * x_norm**3 - 0.1 * x_norm**2)**2)
        
        # Add a cross-term interaction to increase dimensionality complexity
        f10 = 0.15 * np.sum(np.sin(x_norm[:-1] - x_norm[1:]) * np.cos(x_norm[:-1] + x_norm[1:]))
        
        return f1 + 0.35 * f2 + 0.15 * f3 + 0.1 * f4 + 0.07 * f5 + 0.04 * f6 + 0.09 * f7 + 0.02 * f8 + 0.05 * f9 + 0.03 * f10