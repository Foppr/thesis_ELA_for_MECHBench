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
        f2 = np.sum(1.0 / (np.log(np.abs(x) + 1.1)) * np.sin(10.0 * x))
        
        # Multi-scale sinusoidal modulations with exponentially decaying amplitudes
        f3 = 0.5 * np.sum(np.sin(20.0 * x) * np.exp(-0.2 * np.abs(x)) + 
                          np.cos(30.0 * x) * np.exp(-0.1 * np.abs(x)) + 
                          np.sin(50.0 * x) * np.exp(-0.05 * np.abs(x)))
        
        # Chaotic component with polynomial scaling and trigonometric mixing
        f4 = 0.3 * np.sum((x**2 + 0.1 * x)**2 * np.cos(15.0 * x) * np.sin(8.0 * x))
        
        # Fractal-like structure with self-similar peaks at different scales
        f5 = 0.2 * np.sum(np.sin(40.0 * x) * np.cos(25.0 * x) * np.exp(-0.1 * x**2) + 
                          np.sin(60.0 * x) * np.cos(35.0 * x) * np.exp(-0.05 * x**2))
        
        # Non-smooth regions created by absolute value and fractional powers
        f6 = 0.15 * np.sum(np.abs(x)**1.7 + np.abs(x)**2.3)
        
        # High-frequency oscillations with varying amplitudes to increase conditioning difficulty
        f7 = 0.25 * np.sum(np.sin(100.0 * x) * np.cos(80.0 * x) * np.exp(-0.02 * x**2))
        
        # Mixed polynomial and exponential terms to create rugged terrain with variable curvature
        f8 = 0.1 * np.sum(x**5 * np.exp(-0.1 * np.abs(x)) + x**6 * np.sin(12.0 * x))
        
        return f1 + f2 + f3 + f4 + f5 + f6 + f7 + f8