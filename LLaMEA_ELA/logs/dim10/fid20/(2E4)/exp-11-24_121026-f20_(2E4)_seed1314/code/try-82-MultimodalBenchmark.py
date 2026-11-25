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
        f2 = np.sum(np.sin(35 * np.pi * x_norm)**6)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**7 * np.cos(5 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.35 * np.sum(np.abs(x_norm)**0.3)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.2 * np.sum(np.sin(40 * x_norm**2) * np.cos(15 * x_norm))
        
        # Add a new chaotic term with modified logistic map-like behavior
        f7 = 0.4 * np.sum(np.sin(np.pi * x_norm * np.sin(30 * x_norm))**5)
        
        # Add a fourth-order polynomial with random coefficients for extra ruggedness
        f8 = 0.06 * np.sum((x_norm**4 + 0.7 * x_norm**3 - 0.5 * x_norm**2 + 0.2 * x_norm)**2)
        
        # Introduce a new chaotic logistic-like component with different parameters for better fitness
        f9 = 0.3 * np.sum(np.sin(7 * np.pi * x_norm * np.sin(22 * x_norm**2))**7)
        
        # Add a new sinusoidal modulation with variable frequency
        f10 = 0.12 * np.sum(np.sin(20 * x_norm * np.cos(8 * x_norm))**4)
        
        # Introduce a fractional polynomial term to enhance non-smoothness
        f11 = 0.08 * np.sum(np.abs(x_norm)**1.7)
        
        # Add a logarithmic barrier for additional complexity near boundaries
        f12 = 0.15 * np.sum(np.log(1 + x_norm**2))
        
        # Mutation: Slightly modify the chaotic logistic-like term (f9) with altered amplitude and frequency
        f9_mutation = 0.42 * np.sum(np.sin(9 * np.pi * x_norm * np.sin(27 * x_norm**2))**7)
        
        # Add a new oscillatory component with exponential decay
        f13 = 0.1 * np.sum(np.exp(-x_norm**2) * np.sin(45 * x_norm)**3)
        
        # Add a fifth-order polynomial term for enhanced complexity
        f14 = 0.05 * np.sum(x_norm**5 * np.cos(3 * np.pi * x_norm))
        
        return f1 + 0.35 * f2 + 0.18 * f3 + 0.12 * f4 + 0.09 * f5 + 0.06 * f6 + 0.12 * f7 + 0.04 * f8 + f9_mutation + 0.05 * f10 + 0.08 * f11 + 0.15 * f12 + 0.07 * f13 + 0.06 * f14