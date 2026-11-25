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
        f2 = np.sum(np.sin(30 * np.pi * x_norm)**7)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**8 * np.cos(6 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.4 * np.sum(np.abs(x_norm)**0.35)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.25 * np.sum(np.sin(35 * x_norm**2) * np.cos(12 * x_norm))
        
        # Add a new chaotic term with modified logistic map-like behavior
        f7 = 0.45 * np.sum(np.sin(np.pi * x_norm * np.sin(25 * x_norm))**6)
        
        # Add a fourth-order polynomial with random coefficients for extra ruggedness
        f8 = 0.07 * np.sum((x_norm**4 + 0.7 * x_norm**3 - 0.5 * x_norm**2 + 0.2 * x_norm)**2)
        
        # Introduce a new chaotic logistic-like component with different parameters for better fitness
        f9 = 0.35 * np.sum(np.sin(6 * np.pi * x_norm * np.sin(18 * x_norm**2))**8)
        
        # Add a new sinusoidal modulation with variable frequency
        f10 = 0.15 * np.sum(np.sin(18 * x_norm * np.cos(7 * x_norm))**5)
        
        # Introduce a novel hybrid chaotic-modulated term for maximum complexity
        f11 = 0.2 * np.sum(np.sin(40 * x_norm * np.sin(10 * x_norm**3)) * np.cos(8 * x_norm**2))
        
        # Add a fifth-order polynomial with high-frequency oscillations
        f12 = 0.05 * np.sum((x_norm**5 + 0.5 * x_norm**4 - 0.3 * x_norm**3 + 0.1 * x_norm**2 - 0.05 * x_norm)**3)
        
        # Add a double-chaotic sinusoidal component for enhanced ruggedness
        f13 = 0.18 * np.sum(np.sin(20 * np.pi * x_norm * np.sin(15 * x_norm * np.cos(5 * x_norm)))**4)
        
        return f1 + 0.4 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.08 * f6 + 0.15 * f7 + 0.05 * f8 + 0.1 * f9 + 0.06 * f10 + 0.07 * f11 + 0.04 * f12 + 0.09 * f13