import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine modulation with dynamic frequency
        f2 = np.sum(np.sin(15 * np.pi * x_norm * (1 + 0.3 * np.sin(5 * x_norm)))**4)
        
        # Polynomial with exponential interaction terms and adaptive weights
        f3 = np.sum((x_norm**3 + 0.4 * x_norm**2 - 0.2 * x_norm)**2 * np.exp(-0.5 * x_norm**2))
        
        # Hyperbolic tangent and logistic-like chaotic behavior with enhanced nonlinearity
        f4 = np.sum(np.tanh(7 * x_norm) * np.sin(9 * x_norm)**3)
        
        # Cross-dimensional interaction with dynamic weights and coupling strength
        f5 = 0.6 * np.sum((x_norm[:-1] * x_norm[1:] + 0.2 * (x_norm[:-1] + x_norm[1:]))**4)
        
        # Fractional power and logarithmic barrier for increased ruggedness
        f6 = 0.4 * np.sum(np.abs(x_norm)**1.8 * np.log(1 + np.abs(x_norm)))
        
        # Nested trigonometric chaos with multiple frequencies and coupling
        f7 = 0.3 * np.sum(np.sin(np.pi * x_norm * np.sin(7 * x_norm) * np.cos(4 * x_norm))**6)
        
        # Mixed polynomial and exponential decay with enhanced nonlinearity
        f8 = 0.25 * np.sum((x_norm**4 - 0.7 * x_norm**3 + 0.3 * x_norm**2)**2 * np.exp(-0.3 * x_norm**2))
        
        # Gradient-based chaotic modulation with boundary influence and adaptive scaling
        f9 = 0.2 * np.sum(np.sin(20 * x_norm) * np.cos(10 * x_norm) * np.exp(-0.5 * x_norm**2))
        
        # Multi-scale sinusoidal term for fine-grained complexity and increased challenge
        f10 = 0.15 * np.sum(np.sin(25 * x_norm + np.sin(15 * x_norm))**5)
        
        # Additional chaotic coupling term to increase landscape complexity
        f11 = 0.1 * np.sum(np.sin(3 * x_norm) * np.cos(4 * x_norm) * np.sin(6 * x_norm))
        
        return f1 + 0.4 * f2 + 0.25 * f3 + 0.2 * f4 + 0.15 * f5 + 0.15 * f6 + 0.2 * f7 + 0.1 * f8 + 0.15 * f9 + 0.1 * f10 + 0.05 * f11