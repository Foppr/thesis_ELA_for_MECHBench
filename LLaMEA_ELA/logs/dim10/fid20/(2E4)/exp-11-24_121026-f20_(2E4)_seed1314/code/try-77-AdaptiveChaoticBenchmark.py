import numpy as np

class AdaptiveChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        # Precompute scaling factors for each dimension
        self.scaling = np.random.uniform(0.5, 2.0, dim)
        
    def f(self, x):
        # Normalize input to [-1, 1]
        x_norm = x / 5.0
        
        # Polynomial base with conditioning
        f1 = np.sum((x_norm * self.scaling)**4)
        
        # Trigonometric terms with varying frequencies
        f2 = np.sum(np.sin(10 * x_norm * self.scaling) * np.cos(7 * x_norm * self.scaling))
        
        # Chaotic component using sine of quadratic form
        f3 = np.sum(np.sin(np.pi * (x_norm * self.scaling)**2) * np.exp(-0.5 * (x_norm * self.scaling)**2))
        
        # Nested multimodal structure with adaptive peaks
        f4 = np.sum(np.sin(25 * x_norm * self.scaling) * np.cos(15 * x_norm * self.scaling) * 
                   np.exp(-0.1 * (x_norm * self.scaling)**2))
        
        # Asymmetric barrier terms
        f5 = np.sum((np.abs(x_norm * self.scaling) + 0.1)**3 - 0.5 * np.abs(x_norm * self.scaling))
        
        # Fractional power terms for non-smooth behavior
        f6 = np.sum(np.abs(x_norm * self.scaling)**1.3)
        
        # Adaptive logistic-like modulation
        f7 = np.sum(np.sin(np.pi * x_norm * self.scaling * np.sin(20 * x_norm * self.scaling))**3)
        
        # Coupled oscillators with dynamic frequency
        f8 = np.sum(np.sin(12 * x_norm * self.scaling + 0.5 * np.sin(8 * x_norm * self.scaling))**2)
        
        # Exponential modulation with local minima
        f9 = np.sum(np.exp(-0.3 * (x_norm * self.scaling)**2) * np.cos(18 * x_norm * self.scaling))
        
        # Combined weighted sum with dynamic coefficients
        return (0.5 * f1 + 0.3 * f2 + 0.2 * f3 + 0.25 * f4 + 
                0.15 * f5 + 0.1 * f6 + 0.18 * f7 + 0.12 * f8 + 0.08 * f9)