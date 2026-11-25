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
        f2 = np.sum(np.sin(50 * np.pi * x_norm)**8)
        
        # Exponential barrier terms to create rugged landscape
        f3 = np.sum(np.exp(-x_norm**2) - 1.0)
        
        # Mixed polynomial and trigonometric terms for additional complexity
        f4 = np.sum(x_norm**9 * np.cos(7 * np.pi * x_norm))
        
        # Add a global repulsion term to prevent easy convergence
        f5 = 0.5 * np.sum(np.abs(x_norm)**0.4)
        
        # Additional high-frequency component for increased complexity
        f6 = 0.3 * np.sum(np.sin(45 * x_norm**2) * np.cos(15 * x_norm))
        
        # Add a new chaotic term with modified logistic map-like behavior
        f7 = 0.5 * np.sum(np.sin(np.pi * x_norm * np.sin(30 * x_norm))**6)
        
        # Add a fourth-order polynomial with random coefficients for extra ruggedness
        f8 = 0.1 * np.sum((x_norm**4 + 0.8 * x_norm**3 - 0.6 * x_norm**2 + 0.3 * x_norm)**2)
        
        # Introduce a new chaotic logistic-like component with different parameters for better fitness
        f9 = 0.4 * np.sum(np.sin(8 * np.pi * x_norm * np.sin(22 * x_norm**2))**9)
        
        # Add a new sinusoidal modulation with variable frequency
        f10 = 0.18 * np.sum(np.sin(25 * x_norm * np.cos(9 * x_norm))**5)
        
        # Introduce a fractional polynomial term to enhance non-smoothness
        f11 = 0.12 * np.sum(np.abs(x_norm)**1.9)
        
        # Add a logarithmic barrier for additional complexity near boundaries
        f12 = 0.2 * np.sum(np.log(1 + x_norm**2))
        
        # New: Introduce cross-dimensional interaction terms for higher complexity
        f13 = 0.15 * np.sum((x_norm[:-1] + x_norm[1:]) ** 4)
        
        # New: Add a quintic chaotic term with multiple nested frequencies
        f14 = 0.25 * np.sum(np.sin(3 * np.pi * x_norm * np.sin(15 * x_norm) * np.sin(25 * x_norm))**5)
        
        # New: Introduce a hyperbolic tangent modulation for enhanced nonlinearity
        f15 = 0.1 * np.sum(np.tanh(10 * x_norm)**3)
        
        # New: Introduce a new chaotic sine term with increased frequency and modified amplitude
        f16 = 0.3 * np.sum(np.sin(60 * x_norm * np.sin(20 * x_norm**3))**7)
        
        # New: Add a new interaction term with cubic cross-terms for enhanced complexity
        f17 = 0.1 * np.sum((x_norm[:-2] + x_norm[1:-1] + x_norm[2:]) ** 3)
        
        # New: Introduce a modified Gaussian-like barrier for additional ruggedness
        f18 = 0.25 * np.sum(np.exp(-x_norm**4) - 1.0)
        
        return f1 + 0.4 * f2 + 0.2 * f3 + 0.15 * f4 + 0.12 * f5 + 0.05 * f6 + 0.15 * f7 + 0.05 * f8 + 0.2 * f9 + 0.08 * f10 + 0.1 * f11 + 0.2 * f12 + 0.1 * f13 + 0.15 * f14 + 0.08 * f15 + 0.1 * f16 + 0.05 * f17 + 0.15 * f18