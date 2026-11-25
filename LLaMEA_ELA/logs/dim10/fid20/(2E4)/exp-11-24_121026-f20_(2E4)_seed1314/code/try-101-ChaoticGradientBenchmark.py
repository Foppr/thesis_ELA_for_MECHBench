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
        f2 = np.sum(np.sin(12 * np.pi * x_norm * (1 + 0.6 * np.sin(4 * x_norm)))**4)
        
        # Polynomial with exponential interaction terms - modified exponents
        f3 = np.sum((x_norm**4 + 0.4 * x_norm**3 - 0.2 * x_norm)**2 * np.exp(-x_norm**2))
        
        # Hyperbolic tangent and logistic-like chaotic behavior
        f4 = np.sum(np.tanh(6 * x_norm) * np.sin(8 * x_norm)**3)
        
        # Cross-dimensional interaction with dynamic weights - altered coefficients
        f5 = 0.6 * np.sum((x_norm[:-1] * x_norm[1:] + 0.15 * (x_norm[:-1] + x_norm[1:]))**3)
        
        # Fractional power and logarithmic barrier for ruggedness - modified exponent
        f6 = 0.4 * np.sum(np.abs(x_norm)**1.8 * np.log(1 + np.abs(x_norm)))
        
        # Nested trigonometric chaos with multiple frequencies - altered frequencies
        f7 = 0.3 * np.sum(np.sin(np.pi * x_norm * np.sin(6 * x_norm) * np.cos(4 * x_norm))**6)
        
        # Mixed polynomial and exponential decay for nonlinearity - modified coefficients
        f8 = 0.25 * np.sum((x_norm**5 - 0.7 * x_norm**4 + 0.3 * x_norm**3)**2 * np.exp(-0.6 * x_norm**2))
        
        # Gradient-based chaotic modulation with boundary influence - modified frequencies
        f9 = 0.2 * np.sum(np.sin(18 * x_norm) * np.cos(9 * x_norm) * np.exp(-x_norm**2))
        
        # Multi-scale sinusoidal term for fine-grained complexity - altered frequency
        f10 = 0.12 * np.sum(np.sin(25 * x_norm + np.sin(12 * x_norm))**5)
        
        return f1 + 0.35 * f2 + 0.25 * f3 + 0.18 * f4 + 0.12 * f5 + 0.12 * f6 + 0.18 * f7 + 0.1 * f8 + 0.12 * f9 + 0.06 * f10