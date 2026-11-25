import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine modulation with nested logistic map coupling and dynamic scaling
        logistic_map = 4 * x_norm * (1 - x_norm)
        f2 = np.sum(np.sin(15 * np.pi * x_norm * (1 + 0.7 * np.sin(5 * logistic_map)))**5)
        
        # Modified polynomial with exponential interaction terms, chaotic feedback, and enhanced ruggedness
        f3 = np.sum((x_norm**4 + 0.6 * x_norm**3 - 0.4 * x_norm**2)**2 * np.exp(-x_norm**2) * (1 + 0.2 * np.sin(9 * x_norm)))
        
        # Hyperbolic tangent and logistic-like chaotic behavior with dynamic scaling and enhanced coupling
        f4 = np.sum(np.tanh(7 * x_norm) * np.sin(9 * x_norm)**4 * (1 + 0.3 * np.cos(13 * x_norm)))
        
        # Cross-dimensional interaction with nested chaotic weights and enhanced nonlinearity
        weights = np.exp(-np.abs(x_norm[:-1] - x_norm[1:])**2)
        f5 = 0.7 * np.sum((x_norm[:-1] * x_norm[1:] + 0.2 * (x_norm[:-1] + x_norm[1:]))**4 * weights)
        
        # Fractional power and logarithmic barrier with enhanced chaotic modulation
        f6 = 0.4 * np.sum(np.abs(x_norm)**1.9 * np.log(1 + np.abs(x_norm)) * (1 + 0.2 * np.sin(11 * x_norm)))
        
        # Nested trigonometric chaos with multiple frequencies, chaotic coupling, and enhanced complexity
        f7 = 0.35 * np.sum(np.sin(np.pi * x_norm * np.sin(7 * x_norm) * np.cos(4 * logistic_map))**7)
        
        # Mixed polynomial and exponential decay with multi-scale modulation and enhanced ruggedness
        f8 = 0.3 * np.sum((x_norm**5 - 0.9 * x_norm**4 + 0.3 * x_norm**3)**2 * np.exp(-0.6 * x_norm**2) * (1 + 0.15 * np.cos(8 * x_norm)))
        
        # Enhanced gradient-based chaotic modulation with boundary influence and stronger feedback
        f9 = 0.2 * np.sum(np.sin(18 * x_norm) * np.cos(10 * x_norm) * np.exp(-x_norm**2) * (1 + 0.15 * np.sin(15 * x_norm)))
        
        # Multi-scale sinusoidal term for fine-grained complexity with enhanced amplitude modulation
        f10 = 0.15 * np.sum(np.sin(25 * x_norm + np.sin(12 * x_norm))**6 * (1 + 0.25 * np.cos(19 * x_norm)))
        
        # Additional chaotic coupling term with nested logistic dynamics and enhanced complexity
        f11 = 0.12 * np.sum(np.sin(logistic_map * 4) * np.cos(logistic_map * 6) * (1 + 0.15 * np.sin(5 * x_norm)))
        
        # Additional chaotic modulation with higher frequency components for increased ruggedness
        f12 = 0.08 * np.sum(np.sin(22 * x_norm) * np.cos(14 * x_norm) * (1 + 0.1 * np.sin(16 * x_norm)))
        
        return f1 + 0.4 * f2 + 0.3 * f3 + 0.2 * f4 + 0.15 * f5 + 0.15 * f6 + 0.2 * f7 + 0.1 * f8 + 0.15 * f9 + 0.08 * f10 + 0.12 * f11 + 0.05 * f12