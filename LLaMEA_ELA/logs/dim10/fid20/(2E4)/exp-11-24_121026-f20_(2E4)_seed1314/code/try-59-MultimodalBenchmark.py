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
        f4 = np.sum(x_norm**9 * np.cos(8 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.5 * np.sum(np.abs(x_norm)**0.3)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.2 * np.sum(np.sin(30 * x_norm**2) * np.cos(10 * x_norm))
        
        # Add a new chaotic term with modified logistic map-like behavior
        f7 = 0.4 * np.sum(np.sin(np.pi * x_norm * np.sin(20 * x_norm))**5)
        
        # Add a fourth-order polynomial with random coefficients for extra ruggedness
        f8 = 0.08 * np.sum((x_norm**5 + 0.6 * x_norm**4 - 0.4 * x_norm**3 + 0.2 * x_norm)**2)
        
        # Introduce a new chaotic logistic-like component with different parameters for better fitness
        f9 = 0.3 * np.sum(np.sin(5 * np.pi * x_norm * np.sin(15 * x_norm**2))**7)
        
        # Add a new sinusoidal modulation with variable frequency
        f10 = 0.15 * np.sum(np.sin(15 * x_norm * np.cos(6 * x_norm))**4)
        
        # Cross-dimensional interaction terms for increased complexity
        f11 = 0.2 * np.sum(np.sin(np.pi * x_norm * np.sin(25 * x_norm**3))**3)
        
        # Additional high-frequency chaotic component
        f12 = 0.18 * np.sum(np.cos(35 * x_norm) * np.sin(18 * x_norm**2))
        
        return f1 + 0.5 * f2 + 0.25 * f3 + 0.15 * f4 + 0.1 * f5 + 0.07 * f6 + 0.15 * f7 + 0.05 * f8 + 0.1 * f9 + 0.06 * f10 + 0.08 * f11 + 0.04 * f12