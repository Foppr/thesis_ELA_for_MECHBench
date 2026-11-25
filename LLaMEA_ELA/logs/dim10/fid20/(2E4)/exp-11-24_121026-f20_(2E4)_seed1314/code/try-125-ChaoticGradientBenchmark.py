import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Normalize input to [-1, 1] for stability
        x_norm = x / 5.0
        
        # Quadratic base term for conditioning
        f1 = np.sum(x_norm**2)
        
        # Enhanced chaotic sine modulation with nested logistic map coupling and altered frequencies
        logistic_map = 4 * x_norm * (1 - x_norm)
        f2 = np.sum(np.sin(25 * np.pi * x_norm * (1 + 0.7 * np.sin(8 * logistic_map)))**3)
        
        # Modified polynomial with exponential interaction terms, chaotic feedback and adjusted weights
        f3 = np.sum((x_norm**3 + 0.6 * x_norm**2 - 0.4 * x_norm)**2 * np.exp(-0.8 * x_norm**2) * (1 + 0.3 * np.sin(12 * x_norm)))
        
        # Hyperbolic tangent and logistic-like chaotic behavior with dynamic scaling and modified coupling
        f4 = np.sum(np.tanh(9 * x_norm) * np.sin(13 * x_norm)**2 * (1 + 0.4 * np.cos(16 * x_norm)))
        
        # Enhanced cross-dimensional interaction with nested chaotic weights and altered coupling
        weights = np.exp(-np.abs(x_norm[:-1] - x_norm[1:]))
        f5 = 0.8 * np.sum((x_norm[:-1] * x_norm[1:] + 0.3 * (x_norm[:-1] + x_norm[1:]))**3 * weights)
        
        # Fractional power and logarithmic barrier with enhanced chaotic modulation and modified exponents
        f6 = 0.6 * np.sum(np.abs(x_norm)**2.2 * np.log(1 + np.abs(x_norm)) * (1 + 0.3 * np.sin(14 * x_norm)))
        
        # Enhanced nested trigonometric chaos with multiple frequencies, chaotic coupling and altered amplitudes
        f7 = 0.5 * np.sum(np.sin(np.pi * x_norm * np.sin(10 * x_norm) * np.cos(7 * logistic_map))**5)
        
        # Mixed polynomial and exponential decay with multi-scale modulation and adjusted parameters
        f8 = 0.4 * np.sum((x_norm**4 - 0.9 * x_norm**3 + 0.4 * x_norm**2)**2 * np.exp(-0.8 * x_norm**2) * (1 + 0.3 * np.cos(11 * x_norm)))
        
        # Enhanced gradient-based chaotic modulation with boundary influence, chaotic feedback and altered frequencies
        f9 = 0.3 * np.sum(np.sin(25 * x_norm) * np.cos(14 * x_norm) * np.exp(-0.8 * x_norm**2) * (1 + 0.3 * np.sin(19 * x_norm)))
        
        # Enhanced multi-scale sinusoidal term for fine-grained complexity with chaotic amplitude modulation and modified frequencies
        f10 = 0.25 * np.sum(np.sin(35 * x_norm + np.sin(16 * x_norm))**4 * (1 + 0.4 * np.cos(23 * x_norm)))
        
        # Additional enhanced chaotic coupling term with nested logistic dynamics, altered coupling strength and frequencies
        f11 = 0.2 * np.sum(np.sin(logistic_map * 6) * np.cos(logistic_map * 9) * (1 + 0.3 * np.sin(7 * x_norm)))
        
        return f1 + 0.5 * f2 + 0.3 * f3 + 0.25 * f4 + 0.2 * f5 + 0.2 * f6 + 0.25 * f7 + 0.15 * f8 + 0.2 * f9 + 0.15 * f10 + 0.2 * f11