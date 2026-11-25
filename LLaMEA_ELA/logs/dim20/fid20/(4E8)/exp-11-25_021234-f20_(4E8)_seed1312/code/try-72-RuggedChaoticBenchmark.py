import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base quadratic term for conditioning
        f1 = 0.5 * np.sum(x**2)
        
        # Polynomial chaos component with varying degrees
        f2 = 0.3 * np.sum((x**2 + x**4 + x**6) * np.sin(7.0 * x))
        
        # Logarithmic barrier to enhance non-smooth regions
        f3 = 0.2 * np.sum(np.log(1.0 + np.abs(x)) * np.cos(15.0 * x))
        
        # Multi-scale sinusoidal modulations with varying frequencies
        f4 = 0.25 * np.sum(np.sin(20.0 * x) * np.cos(10.0 * x) * np.sin(5.0 * x))
        
        # Chaotic modulation with exponential decay and fractal-like behavior
        f5 = 0.18 * np.sum(np.exp(-0.2 * x**2) * np.sin(25.0 * x) * np.cos(18.0 * x))
        
        # Ruggedness through high-frequency oscillations
        f6 = 0.15 * np.sum(np.sin(30.0 * x) * np.cos(22.0 * x) * np.sin(14.0 * x) * np.cos(8.0 * x))
        
        # Multi-scale peaks and valleys with overlapping modulations
        f7 = 0.12 * np.sum(np.sin(35.0 * x) * np.cos(28.0 * x) * np.sin(16.0 * x) * np.cos(9.0 * x))
        
        # Additional cubic and quartic terms for enhanced complexity
        f8 = 0.08 * np.sum(x**3 * np.cos(12.0 * x) + x**4 * np.sin(8.0 * x))
        
        # Saddle point structure with mixed trigonometric interactions
        f9 = 0.06 * np.sum(np.sin(9.0 * x) * np.cos(17.0 * x) * x**2)
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9