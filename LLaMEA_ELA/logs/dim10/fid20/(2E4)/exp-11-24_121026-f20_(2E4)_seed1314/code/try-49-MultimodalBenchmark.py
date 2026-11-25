import numpy as np

class MultimodalBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic term with conditioning
        f1 = np.sum(x_norm**2)
        
        # High-frequency cosine terms creating multiple local minima
        f2 = np.sum(np.cos(10 * np.pi * x_norm)**6)
        
        # Polynomial interaction terms for additional complexity
        f3 = np.sum((x_norm**3 + 0.5 * x_norm**2 - 0.3 * x_norm)**4)
        
        # Exponential barrier terms to create rugged landscape
        f4 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Chaotic perturbation using a modified sine-logistic map
        f5 = 0.5 * np.sum(np.sin(np.pi * x_norm * np.log(1 + 10 * np.abs(x_norm)))**3)
        
        # Mixed trigonometric and polynomial term for extra ruggedness
        f6 = 0.2 * np.sum(np.sin(5 * x_norm) * x_norm**3)
        
        # Add a fourth-order polynomial with random coefficients
        f7 = 0.1 * np.sum((x_norm**4 - 0.5 * x_norm**3 + 0.2 * x_norm**2 - 0.1 * x_norm)**2)
        
        # Additional high-frequency component for increased complexity
        f8 = 0.3 * np.sum(np.cos(15 * x_norm**2) * np.sin(7 * x_norm))
        
        return f1 + 0.3 * f2 + 0.2 * f3 + 0.1 * f4 + 0.08 * f5 + 0.05 * f6 + 0.03 * f7 + 0.04 * f8