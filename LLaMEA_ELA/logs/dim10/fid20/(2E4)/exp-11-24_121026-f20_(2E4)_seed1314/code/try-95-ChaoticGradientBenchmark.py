import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine modulation with varying frequency based on dimension
        f2 = np.sum(np.sin(10 * np.pi * x_norm * (1 + 0.5 * np.sin(3 * x_norm)))**4)
        
        # Polynomial with exponential interaction terms
        f3 = np.sum((x_norm**3 + 0.5 * x_norm**2 - 0.3 * x_norm)**2 * np.exp(-x_norm**2))
        
        # Hyperbolic tangent and logistic-like chaotic behavior
        f4 = np.sum(np.tanh(5 * x_norm) * np.sin(7 * x_norm)**3)
        
        # Cross-dimensional interaction with dynamic weights
        f5 = 0.5 * np.sum((x_norm[:-1] * x_norm[1:] + 0.1 * (x_norm[:-1] + x_norm[1:]))**3)
        
        # Fractional power and logarithmic barrier for ruggedness
        f6 = 0.3 * np.sum(np.abs(x_norm)**1.7 * np.log(1 + np.abs(x_norm)))
        
        # Nested trigonometric chaos with multiple frequencies
        f7 = 0.25 * np.sum(np.sin(np.pi * x_norm * np.sin(5 * x_norm) * np.cos(3 * x_norm))**6)
        
        # Mixed polynomial and exponential decay for nonlinearity
        f8 = 0.2 * np.sum((x_norm**4 - 0.8 * x_norm**3 + 0.2 * x_norm**2)**2 * np.exp(-0.5 * x_norm**2))
        
        # Gradient-based chaotic modulation with boundary influence
        f9 = 0.15 * np.sum(np.sin(15 * x_norm) * np.cos(8 * x_norm) * np.exp(-x_norm**2))
        
        # Multi-scale sinusoidal term for fine-grained complexity
        f10 = 0.1 * np.sum(np.sin(20 * x_norm + np.sin(10 * x_norm))**5)
        
        return f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.1 * f6 + 0.15 * f7 + 0.08 * f8 + 0.1 * f9 + 0.05 * f10