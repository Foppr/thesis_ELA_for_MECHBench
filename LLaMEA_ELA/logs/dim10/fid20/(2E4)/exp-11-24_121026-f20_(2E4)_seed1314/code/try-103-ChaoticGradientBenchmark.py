import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Chaotic sine modulation with logistic map coupling
        logistic_map = 4 * x_norm * (1 - x_norm)
        f2 = np.sum(np.sin(10 * np.pi * x_norm * (1 + 0.5 * np.sin(3 * logistic_map)))**4)
        
        # Polynomial with exponential interaction terms and chaotic feedback
        f3 = np.sum((x_norm**3 + 0.5 * x_norm**2 - 0.3 * x_norm)**2 * np.exp(-x_norm**2) * (1 + 0.1 * np.sin(7 * x_norm)))
        
        # Hyperbolic tangent and logistic-like chaotic behavior with dynamic scaling
        f4 = np.sum(np.tanh(5 * x_norm) * np.sin(7 * x_norm)**3 * (1 + 0.2 * np.cos(11 * x_norm)))
        
        # Cross-dimensional interaction with nested chaotic weights
        weights = np.exp(-np.abs(x_norm[:-1] - x_norm[1:]))
        f5 = 0.5 * np.sum((x_norm[:-1] * x_norm[1:] + 0.1 * (x_norm[:-1] + x_norm[1:]))**3 * weights)
        
        # Fractional power and logarithmic barrier with chaotic modulation
        f6 = 0.3 * np.sum(np.abs(x_norm)**1.7 * np.log(1 + np.abs(x_norm)) * (1 + 0.15 * np.sin(9 * x_norm)))
        
        # Nested trigonometric chaos with multiple frequencies and chaotic coupling
        f7 = 0.25 * np.sum(np.sin(np.pi * x_norm * np.sin(5 * x_norm) * np.cos(3 * logistic_map))**6)
        
        # Mixed polynomial and exponential decay with multi-scale modulation
        f8 = 0.2 * np.sum((x_norm**4 - 0.8 * x_norm**3 + 0.2 * x_norm**2)**2 * np.exp(-0.5 * x_norm**2) * (1 + 0.1 * np.cos(6 * x_norm)))
        
        # Gradient-based chaotic modulation with boundary influence and chaotic feedback
        f9 = 0.15 * np.sum(np.sin(15 * x_norm) * np.cos(8 * x_norm) * np.exp(-x_norm**2) * (1 + 0.1 * np.sin(13 * x_norm)))
        
        # Multi-scale sinusoidal term for fine-grained complexity with chaotic amplitude modulation
        f10 = 0.1 * np.sum(np.sin(20 * x_norm + np.sin(10 * x_norm))**5 * (1 + 0.2 * np.cos(17 * x_norm)))
        
        # Additional chaotic coupling term with nested logistic dynamics
        f11 = 0.08 * np.sum(np.sin(logistic_map * 3) * np.cos(logistic_map * 5) * (1 + 0.1 * np.sin(4 * x_norm)))
        
        return f1 + 0.3 * f2 + 0.2 * f3 + 0.15 * f4 + 0.1 * f5 + 0.1 * f6 + 0.15 * f7 + 0.08 * f8 + 0.1 * f9 + 0.05 * f10 + 0.1 * f11