import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine modulation with nested logistic map coupling
        logistic_map = 4 * x_norm * (1 - x_norm)
        f2 = np.sum(np.sin(15 * np.pi * x_norm * (1 + 0.7 * np.sin(5 * logistic_map)))**4)
        
        # Modified polynomial with exponential interaction terms and chaotic feedback
        f3 = np.sum((x_norm**3 + 0.6 * x_norm**2 - 0.4 * x_norm)**2 * np.exp(-0.8 * x_norm**2) * (1 + 0.15 * np.sin(9 * x_norm)))
        
        # Hyperbolic tangent and logistic-like chaotic behavior with dynamic scaling
        f4 = np.sum(np.tanh(7 * x_norm) * np.sin(9 * x_norm)**3 * (1 + 0.25 * np.cos(13 * x_norm)))
        
        # Enhanced cross-dimensional interaction with nested chaotic weights
        weights = np.exp(-np.abs(x_norm[:-1] - x_norm[1:]))
        f5 = 0.6 * np.sum((x_norm[:-1] * x_norm[1:] + 0.15 * (x_norm[:-1] + x_norm[1:]))**3 * weights)
        
        # Fractional power and logarithmic barrier with enhanced chaotic modulation
        f6 = 0.4 * np.sum(np.abs(x_norm)**1.8 * np.log(1 + np.abs(x_norm)) * (1 + 0.2 * np.sin(11 * x_norm)))
        
        # Enhanced nested trigonometric chaos with multiple frequencies and chaotic coupling
        f7 = 0.3 * np.sum(np.sin(np.pi * x_norm * np.sin(7 * x_norm) * np.cos(5 * logistic_map))**6)
        
        # Mixed polynomial and exponential decay with multi-scale modulation
        f8 = 0.25 * np.sum((x_norm**4 - 0.9 * x_norm**3 + 0.25 * x_norm**2)**2 * np.exp(-0.6 * x_norm**2) * (1 + 0.15 * np.cos(8 * x_norm)))
        
        # Enhanced gradient-based chaotic modulation with boundary influence and chaotic feedback
        f9 = 0.2 * np.sum(np.sin(18 * x_norm) * np.cos(10 * x_norm) * np.exp(-0.8 * x_norm**2) * (1 + 0.15 * np.sin(15 * x_norm)))
        
        # Enhanced multi-scale sinusoidal term for fine-grained complexity with chaotic amplitude modulation
        f10 = 0.15 * np.sum(np.sin(25 * x_norm + np.sin(12 * x_norm))**5 * (1 + 0.25 * np.cos(19 * x_norm)))
        
        # Additional enhanced chaotic coupling term with nested logistic dynamics
        f11 = 0.1 * np.sum(np.sin(logistic_map * 4) * np.cos(logistic_map * 7) * (1 + 0.15 * np.sin(5 * x_norm)))
        
        return f1 + 0.35 * f2 + 0.25 * f3 + 0.2 * f4 + 0.15 * f5 + 0.15 * f6 + 0.2 * f7 + 0.1 * f8 + 0.15 * f9 + 0.08 * f10 + 0.15 * f11