import numpy as np

class ChaoticGradientBenchmark:
    def __init__(self, dim):
        self.dim = dim
        self.global_min = 0.0
        self.x_opt = np.zeros(dim)
    
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term
        f1 = np.sum(x**2)
        
        # Chaotic sine modulation with exponentially decaying amplitudes
        f2 = np.sum(np.sin(2.0 * np.pi * x) * np.exp(-0.1 * np.abs(x)) * np.cos(3.0 * np.pi * x))
        
        # Multi-scale sinusoidal component with varying frequencies and amplitudes
        f3 = np.sum(np.sin(10.0 * x) * np.cos(15.0 * x) * np.sin(25.0 * x) * np.exp(-0.05 * x**2))
        
        # Gradient-based interaction with exponential decay and multi-frequency modulation
        grad_interaction = np.sum(np.exp(-0.5 * (x[:-1] - x[1:])**2) * np.sin(20.0 * (x[:-1] + x[1:])) * np.cos(10.0 * (x[:-1] - x[1:])))
        
        # Fractional power chaotic component with recursive structure
        f4 = np.sum(np.abs(x)**1.7 * np.sin(5.0 * np.pi * x) * np.cos(7.0 * np.pi * x) * np.exp(-0.2 * np.abs(x)))
        
        # Non-separable term with exponentially weighted cross-terms
        f5 = np.sum(np.exp(-0.3 * np.abs(x[:-1] - x[1:])) * np.sin(12.0 * (x[:-1] * x[1:])) * np.cos(8.0 * (x[:-1] + x[1:])))
        
        # Multi-scale fractal-like component with varying correlation lengths
        f6 = np.sum(np.sin(20.0 * x) * np.cos(25.0 * x) * np.sin(30.0 * x) * np.exp(-0.1 * np.abs(x)**1.5))
        
        # Combined function with dynamic weighting and chaotic amplification
        return 0.25 * f1 + 0.20 * f2 + 0.18 * f3 + 0.15 * grad_interaction + 0.12 * f4 + 0.10 * f5 + 0.08 * f6