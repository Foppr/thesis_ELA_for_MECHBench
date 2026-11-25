import numpy as np

class ChaoticInterferenceBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Logarithmic barrier terms to create sharp gradients near boundaries
        f2 = 0.3 * np.sum(-np.log(25.0 - x**2) * (x**2 < 25.0))
        
        # Trigonometric wave interference with varying amplitudes and frequencies
        f3 = 0.4 * np.sum(np.sin(15.0 * x) * np.cos(10.0 * x) * np.exp(-0.1 * x**2))
        
        # Chaotic modulation using logistic map-like behavior
        f4 = 0.2 * np.sum(np.sin(20.0 * x + np.sin(17.0 * x)) * np.cos(13.0 * x))
        
        # Adaptive noise component that varies with input magnitude
        noise = np.random.normal(0, 0.05 * (1 + np.abs(x)), self.dim)
        f5 = 0.1 * np.sum(noise * np.sin(8.0 * x))
        
        # Fractal-like structure using multiple sine waves with different periods
        f6 = 0.25 * np.sum(np.sin(25.0 * x) * np.cos(22.0 * x) * np.sin(19.0 * x))
        
        # Non-smooth regions created by absolute value and floor operations
        f7 = 0.15 * np.sum(np.abs(x) * np.sin(12.0 * x) + np.floor(x) * np.cos(9.0 * x))
        
        # Exponential decay with sinusoidal oscillation to create complex valleys
        f8 = 0.3 * np.sum(np.exp(-0.5 * x**2) * np.sin(14.0 * x) * np.cos(7.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8