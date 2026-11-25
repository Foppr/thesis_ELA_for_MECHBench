import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial with fractional exponents to introduce non-smoothness
        f1 = np.sum(x**3.5 + 0.7 * x**2.8 + 0.3 * x**1.9)
        
        # Logarithmic barrier with chaotic modulation for sharp gradients
        f2 = np.sum(np.log(np.abs(x) + 1.05) * np.sin(15.0 * x) * np.cos(7.0 * x))
        
        # Multi-scale sinusoidal modulations with varying decay rates and frequencies
        f3 = 0.6 * np.sum(np.sin(25.0 * x) * np.exp(-0.3 * np.abs(x)) + 
                          np.cos(40.0 * x) * np.exp(-0.15 * np.abs(x)) + 
                          np.sin(65.0 * x) * np.exp(-0.08 * np.abs(x)))
        
        # Chaotic component with mixed trigonometric and polynomial terms
        f4 = 0.4 * np.sum((x**2 + 0.15 * x)**1.5 * np.cos(20.0 * x) * np.sin(12.0 * x))
        
        # Fractal-like structure with self-similar peaks at multiple scales
        f5 = 0.3 * np.sum(np.sin(50.0 * x) * np.cos(30.0 * x) * np.exp(-0.12 * x**2) + 
                          np.sin(75.0 * x) * np.cos(45.0 * x) * np.exp(-0.08 * x**2))
        
        # Non-smooth regions using fractional powers and absolute value combinations
        f6 = 0.2 * np.sum(np.abs(x)**1.8 + np.abs(x)**2.5 + np.abs(x)**1.3)
        
        # High-frequency oscillations with varying amplitudes and damping
        f7 = 0.3 * np.sum(np.sin(120.0 * x) * np.cos(90.0 * x) * np.exp(-0.03 * x**2))
        
        # Mixed polynomial and exponential terms with variable curvature
        f8 = 0.15 * np.sum(x**4.5 * np.exp(-0.15 * np.abs(x)) + x**5.5 * np.sin(15.0 * x))
        
        # Slight mutation: adjusting coefficients and adding a new chaotic interaction term
        f9 = 0.25 * np.sum(np.sin(80.0 * x) * np.cos(55.0 * x) * np.exp(-0.1 * x**2))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8 + f9