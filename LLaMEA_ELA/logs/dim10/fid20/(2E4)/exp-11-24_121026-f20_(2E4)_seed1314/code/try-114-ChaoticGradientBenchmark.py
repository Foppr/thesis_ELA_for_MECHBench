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
        f2 = np.sum(np.sin(17 * np.pi * x_norm * (1 + 0.6 * np.sin(6 * logistic_map)))**5)
        
        # Modified polynomial with exponential interaction terms, chaotic feedback, and enhanced ruggedness
        f3 = np.sum((x_norm**4 + 0.5 * x_norm**3 - 0.3 * x_norm**2)**2 * np.exp(-x_norm**2) * (1 + 0.25 * np.sin(10 * x_norm)))
        
        # Hyperbolic tangent and logistic-like chaotic behavior with dynamic scaling and enhanced coupling
        f4 = np.sum(np.tanh(8 * x_norm) * np.sin(10 * x_norm)**4 * (1 + 0.35 * np.cos(14 * x_norm)))
        
        # Cross-dimensional interaction with nested chaotic weights and enhanced nonlinearity
        weights = np.exp(-np.abs(x_norm[:-1] - x_norm[1:])**2)
        f5 = 0.8 * np.sum((x_norm[:-1] * x_norm[1:] + 0.25 * (x_norm[:-1] + x_norm[1:]))**4 * weights)
        
        # Fractional power and logarithmic barrier with enhanced chaotic modulation
        f6 = 0.5 * np.sum(np.abs(x_norm)**1.8 * np.log(1 + np.abs(x_norm)) * (1 + 0.25 * np.sin(12 * x_norm)))
        
        # Nested trigonometric chaos with multiple frequencies, chaotic coupling, and enhanced complexity
        f7 = 0.4 * np.sum(np.sin(np.pi * x_norm * np.sin(8 * x_norm) * np.cos(5 * logistic_map))**7)
        
        # Mixed polynomial and exponential decay with multi-scale modulation and enhanced ruggedness
        f8 = 0.35 * np.sum((x_norm**5 - 0.8 * x_norm**4 + 0.25 * x_norm**3)**2 * np.exp(-0.7 * x_norm**2) * (1 + 0.2 * np.cos(9 * x_norm)))
        
        # Enhanced gradient-based chaotic modulation with boundary influence and stronger feedback
        f9 = 0.25 * np.sum(np.sin(19 * x_norm) * np.cos(11 * x_norm) * np.exp(-x_norm**2) * (1 + 0.2 * np.sin(16 * x_norm)))
        
        # Multi-scale sinusoidal term for fine-grained complexity with enhanced amplitude modulation
        f10 = 0.18 * np.sum(np.sin(27 * x_norm + np.sin(13 * x_norm))**6 * (1 + 0.3 * np.cos(20 * x_norm)))
        
        # Additional chaotic coupling term with nested logistic dynamics and enhanced complexity
        f11 = 0.15 * np.sum(np.sin(logistic_map * 4.5) * np.cos(logistic_map * 6.5) * (1 + 0.2 * np.sin(5.5 * x_norm)))
        
        # Additional chaotic modulation with higher frequency components for increased ruggedness
        f12 = 0.1 * np.sum(np.sin(24 * x_norm) * np.cos(15 * x_norm) * (1 + 0.15 * np.sin(17 * x_norm)))
        
        return f1 + 0.38 * f2 + 0.28 * f3 + 0.18 * f4 + 0.16 * f5 + 0.16 * f6 + 0.22 * f7 + 0.12 * f8 + 0.16 * f9 + 0.09 * f10 + 0.13 * f11 + 0.06 * f12