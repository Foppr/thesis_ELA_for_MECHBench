import numpy as np

class ChaoticRidgeBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds [-5, 5]
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = np.sum(x**2) * 0.1
        
        # Chaotic ridge structure with exponential modulation
        f2 = 0.3 * np.sum(np.exp(-0.5 * x**2) * np.sin(3.0 * x)**2)
        
        # Modified trigonometric interaction weights
        f3 = 0.4 * np.sum(np.cos(1.5 * x) * np.sin(2.5 * x) * np.tan(0.8 * x))
        
        # Perturbed polynomial terms with chaotic coefficients
        f4 = 0.25 * np.sum((x**3 + 0.5 * x**2 - 0.3 * x + 0.1)**2)
        
        # Exponential coupling between dimensions with chaotic scaling
        f5 = 0.35 * np.sum(np.exp(-np.abs(x[:-1] - x[1:])) * (x[1:]**2 + x[:-1]**2))
        
        # Nested sinusoidal modulations with varying frequencies
        f6 = 0.2 * np.sum(np.sin(4.0 * x) * np.cos(1.2 * x) * np.sin(0.3 * x))
        
        # Non-smooth gradient transitions using step functions and absolute values
        f7 = 0.15 * np.sum(np.abs(x)**1.7 + np.abs(x)**0.8)
        
        # Self-similar fractal structure with recursive sine components
        f8 = 0.1 * np.sum(np.sin(2.0 * np.sin(3.0 * x)))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8