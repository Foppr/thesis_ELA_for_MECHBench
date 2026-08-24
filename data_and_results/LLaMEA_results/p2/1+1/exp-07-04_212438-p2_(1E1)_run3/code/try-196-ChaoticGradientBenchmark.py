import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic component with variable conditioning
        f1 = 0.5 * np.sum(x**2)
        
        # Chaotic sinusoidal modulation with exponential decay
        f2 = np.sum(np.exp(-0.1 * np.abs(x)) * np.sin(10.0 * x) * np.cos(15.0 * x))
        
        # Multi-scale oscillatory component with varying frequencies
        f3 = np.sum(np.sin(2.0 * x) * np.cos(4.0 * x) * np.sin(8.0 * x) * np.cos(16.0 * x))
        
        # Cross-dimensional coupling with exponential interaction
        f4 = np.sum(np.exp(-0.5 * np.abs(x[:-1] - x[1:])) * np.sin(5.0 * (x[:-1] + x[1:])) * np.cos(3.0 * (x[:-1] - x[1:])))
        
        # Fractal-like recursive structure with diminishing returns
        f5 = np.sum(np.sin(20.0 * x) * np.cos(25.0 * x) * np.exp(-0.05 * x**2) * np.sin(0.5 * np.sum(x**2)))
        
        # High-frequency chaotic component with dynamic phase shifts
        f6 = np.sum(np.sin(30.0 * x) * np.cos(35.0 * x) * np.sin(40.0 * x) * np.cos(45.0 * x) * np.exp(-0.3 * np.abs(x)))
        
        # Asymmetric gradient modulation with non-separable terms
        f7 = np.sum((x[:-1] * x[1:] + 0.5 * x[:-1]**2 + 0.3 * x[1:]**2) * np.exp(-0.2 * np.abs(x[:-1] - x[1:])))
        
        # Combined function with dynamic weighting and normalization
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * f4 + 0.12 * f5 + 0.08 * f6 + 0.02 * f7