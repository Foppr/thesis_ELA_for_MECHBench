import numpy as np

class RuggedChaoticBenchmark:
    def __init__(self, dim):
        self.dim = dim
        
    def f(self, x):
        # Ensure x is within bounds
        x = np.clip(x, -5.0, 5.0)
        
        # Base polynomial term with varying degrees
        f1 = np.sum(x**4 + 0.5 * x**3 + 0.2 * x**2)
        
        # Logarithmic barrier terms to create sharp gradients and narrow valleys
        f2 = np.sum(1.5 / (np.log(np.abs(x) + 1.2)) * np.sin(12.0 * x))
        
        # Multi-scale sinusoidal modulations with exponentially decaying amplitudes
        f3 = 0.6 * np.sum(np.sin(25.0 * x) * np.exp(-0.25 * np.abs(x)) + 
                          np.cos(35.0 * x) * np.exp(-0.15 * np.abs(x)) + 
                          np.sin(45.0 * x) * np.exp(-0.08 * np.abs(x)))
        
        # Chaotic component with polynomial scaling and trigonometric mixing
        f4 = 0.35 * np.sum((x**2 + 0.15 * x)**2 * np.cos(18.0 * x) * np.sin(10.0 * x))
        
        # Fractal-like structure with self-similar peaks at different scales
        f5 = 0.25 * np.sum(np.sin(45.0 * x) * np.cos(30.0 * x) * np.exp(-0.12 * x**2) + 
                           np.sin(65.0 * x) * np.cos(40.0 * x) * np.exp(-0.08 * x**2))
        
        # Non-smooth regions created by absolute value and fractional powers
        f6 = 0.2 * np.sum(np.abs(x)**1.8 + np.abs(x)**2.5)
        
        # High-frequency oscillations with varying amplitudes to increase conditioning difficulty
        f7 = 0.3 * np.sum(np.sin(110.0 * x) * np.cos(90.0 * x) * np.exp(-0.03 * x**2))
        
        # Mixed polynomial and exponential terms to create rugged terrain with variable curvature
        f8 = 0.15 * np.sum(x**5 * np.exp(-0.12 * np.abs(x)) + x**6 * np.sin(14.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8